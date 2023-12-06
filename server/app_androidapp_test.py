from flask import Flask, request, jsonify
import json 
import requests

app = Flask(__name__)

# Current biometric levels
HEART_RATE = 0
STRESS = 0 

def nano_leaf(mood):
    esp32_url = ''

    # Send post request to smart device
    requests.post(esp32_url, json={'mood': mood})

def classify_mood():
    # Thresholding or some ML model to classify mood based on heart rate and stress
    pass

@app.route('/', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        global HEART_RATE, STRESS

        data = json.loads(request.data)

        # https://developer.samsung.com/sdp/blog/en/2022/05/25/check-which-sensor-you-can-use-in-galaxy-watch-running-wear-os-powered-by-samsung
        HEART_RATE = data['BPM']
        isAthlete = data['isAthlete']
        #STRESS = data['stress']

        # mood = classify_mood()
        # trigger_alexa(mood)

        return jsonify({'status': 'ok ' + HEART_RATE + '|' + isAthlete}), 200

    return jsonify({'status': 'bad input'}), 400

def main():
    app.run(debug=True, port=8081)
    
if __name__ == '__main__':
    main()