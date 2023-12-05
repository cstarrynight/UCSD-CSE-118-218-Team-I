from flask import Flask, request, jsonify
import json 
import requests
import numpy as np

app = Flask(__name__)

# Smart device forwarding URL
ESP32_URL = ''

# User Mode 0: Non-Athlete, User Mode 1: Elite Athlete 
USER_MODE = 0 

bpm_buffer = []

def nano_leaf(red, green, blue):

    global ESP32_URL

    url = f'{ESP32_URL}/color?red={red}&green={green}&blue={blue}'

    print("started nano leaf function")

    # Send post request to smart device
    requests.get(url)

    print("nano leaf get")

    return jsonify({'status': 'ok'}), 200

def classify_mood(bpm_values):
    # Thresholding or some ML model to classify mood based on heart rate and stress
    global USER_MODE

    print("started to classify mood")

    hrv = get_hrv(bpm_values)
    avg_hr = np.mean(bpm_values)

    print("hrv and avg_hr obtained")

    # If user is a regular adult
    if USER_MODE == 0: 
        if avg_hr < 60:
            # TODO: low HR
            nano_leaf(255, 0, 0)
        elif avg_hr > 100:
            # TODO: high HR
            nano_leaf(0, 0, 255)
        else:
            nano_leaf(0, 255, 0)

        if hrv < 20:
            # TODO: low HRV, high stress
            pass
        elif hrv > 89:
            # TODO: high HRV
            pass

    # If user is an elite athlete
    else:
        if avg_hr < 40:
            # TODO: dangerously low HR
            pass
        elif avg_hr > 100:
            # TODO: high HR 
            pass  

        if hrv < 20:
            # TODO: low HRV, high stress
            pass
        elif hrv > 100:
            # TODO: high HRV
            pass
    pass

def get_hrv(bpm_values):
    
    print("started to get hrv")

    """ Calculate HRV (Heart Rate Variability) using RMSSD method from BPM (Beats Per Minute) values. """

    def bpm_to_ibi(bpm):
        """ Convert heart rate BPM to IBI (inter-beat intervals in milliseconds). """
        return 60000 / bpm
    
    # Convert BPM values to IBI values
    ibi_values = [bpm_to_ibi(bpm) for bpm in bpm_values]

    # Calculate successive differences between IBIs
    diff_ibi = np.diff(ibi_values)

    # Calculate the square of differences
    squared_diff = np.square(diff_ibi)

    # Calculate the mean of squared differences
    mean_squared_diff = np.mean(squared_diff)

    # Calculate the square root of the mean
    rmssd = np.sqrt(mean_squared_diff)

    return rmssd



@app.route('/', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        data = json.loads(request.data)
        heart_rate = float(data['bpm'])

        bpm_buffer.append(heart_rate)

        if len(bpm_buffer) == 5:
            bpm_values = bpm_buffer.copy()
            bpm_buffer.clear()

            print("buffer is full, classify mood")
            
            # Trigger nano leaf
            classify_mood(bpm_values)

        print("classify mood completed")

        return jsonify({'status': 'ok'}), 200

    return jsonify({'status': 'bad input'}), 400

def run(port, esp32_url):
    global ESP32_URL

    ESP32_URL = esp32_url
    app.run(debug=True, port=port)
    
if __name__ == '__main__':
    run()