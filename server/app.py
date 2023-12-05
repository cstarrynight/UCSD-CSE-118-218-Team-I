from flask import Flask, request, jsonify
import json 
import requests
import numpy as np

app = Flask(__name__)

# Smart device forwarding URL
ESP32_URL = 'http://192.168.1.91/color'

# Current biometric levels
HEART_RATE = 0
STRESS = 0 
USER_MODE = 0 # 0 indicates regular, 1 indicates athlete

@app.route('/color')
def nano_leaf():
    global ESP32_URL
    red = request.args.get('red')
    green = request.args.get('green')
    blue = request.args.get('blue')

    url = f'{ESP32_URL}?red={red}&green={green}&blue={blue}'

    # Send post request to smart device
    response = requests.get(url)
    print(response)

    return jsonify({'status': 'ok'}), 200

def classify_mood(bpm_values):
    # Thresholding or some ML model to classify mood based on heart rate and stress

    hrv = get_hrv(bpm_values)
    avg_hr = np.mean(bpm_values)

    # If user is a regular adult
    if USER_MODE == 0: 
        if avg_hr < 60:
            # TODO: low HR
            pass
        elif avg_hr > 100:
            # TODO: high HR 
            pass  

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
        global HEART_RATE, STRESS

        data = json.loads(request.data)

        # https://developer.samsung.com/sdp/blog/en/2022/05/25/check-which-sensor-you-can-use-in-galaxy-watch-running-wear-os-powered-by-samsung
        #HEART_RATE = data['bpm']
        #STRESS = data['stress']

        # mood = classify_mood()
        # trigger_alexa(mood)

        return jsonify({'status': 'ok'}), 200

    return jsonify({'status': 'bad input'}), 400

def main():
    app.run(debug=True, port=8080)
    
if __name__ == '__main__':
    main()

    # ngrok config edit
    # ngrok start --all