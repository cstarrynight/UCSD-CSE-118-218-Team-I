from flask import Flask, request, jsonify
import json 
import requests

app = Flask(__name__)

# Smart device forwarding URL
ESP32_URL = ''

def nano_leaf(red, green, blue):
    global ESP32_URL

    url = f'{ESP32_URL}/color?red={red}&green={green}&blue={blue}'

    # Send post request to smart device
    requests.get(url)

    return jsonify({'status': 'ok'}), 200

def classify_mood(heart_rate):
    # Thresholding or some ML model to classify mood based on heart rate and stress
    global HEART_RATE

    if heart_rate > 85.0:
        nano_leaf(255, 0, 0)
    else:
        nano_leaf(0, 255, 0)

@app.route('/', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        global HEART_RATE, STRESS

        data = json.loads(request.data)
        heart_rate = float(data['bpm'])
        #stress = float(data['stress'])

        # Trigger nano leaf
        classify_mood(heart_rate)

        return jsonify({'status': 'ok'}), 200

    return jsonify({'status': 'bad input'}), 400

def run(port, esp32_url):
    global ESP32_URL

    ESP32_URL = esp32_url
    app.run(debug=True, port=port)
    
if __name__ == '__main__':
    run()