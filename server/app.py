from flask import Flask, request, jsonify
import json 
import requests

app = Flask(__name__)

# Smart device forwarding URL
ESP32_URL = 'http://172.20.10.3'

# Current biometric levels
HEART_RATE = 0
STRESS = 0 

def nano_leaf(red, green, blue):
    global ESP32_URL

    url = f'{ESP32_URL}/color?red={red}&green={green}&blue={blue}'

    # Send post request to smart device
    requests.get(url)

    return jsonify({'status': 'ok'}), 200

def classify_mood():
    # Thresholding or some ML model to classify mood based on heart rate and stress
    global HEART_RATE
    if HEART_RATE > 85:
        nano_leaf(255, 0, 0)
    else:
        nano_leaf(0, 255, 0)

@app.route('/', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        global HEART_RATE, STRESS

        data = json.loads(request.data)
        HEART_RATE = float(data['bpm'])
        #STRESS = data['stress']

        # Trigger nano leaf
        mood = classify_mood()

        return jsonify({'status': 'ok'}), 200

    return jsonify({'status': 'bad input'}), 400

def main():
    app.run(debug=True, port=8080)
    
if __name__ == '__main__':
    main()

    # ngrok config edit
    # ngrok start --all
    # 172.20.10.3