from flask import Flask, request, jsonify
import json 
import requests

app = Flask(__name__)

# Smart device forwarding URL
ESP32_URL = 'http://192.168.1.91/color'

# Current biometric levels
HEART_RATE = 0
STRESS = 0 

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

def classify_mood():
    # Thresholding or some ML model to classify mood based on heart rate and stress
    pass

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