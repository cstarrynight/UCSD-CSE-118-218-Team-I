from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import json 
import requests

app = Flask(__name__)

# Voiceflow
load_dotenv()
voiceflow_api_key = os.environ.get('VOICEFLOW_API_KEY') 

# Current biometric levels
HEART_RATE = 0
STRESS = 0 

def trigger_alexa(intent):
    # Placeholder unique ID used to track conversation state. Wake Alexa to trigger a device/environment change
    user_id = 'user'
    body = {'action': {'type': 'text', 'payload': intent}}

    # Mimic a wake up call...
    requests.post(
        f"https://general-runtime.voiceflow.com/state/user/{user_id}/interact",
        headers={"Authorization": voiceflow_api_key},
    )

    # Send intent
    response_body = requests.post(
        f"https://general-runtime.voiceflow.com/state/user/{user_id}/interact",
        json=body,
        headers={"Authorization": voiceflow_api_key},
    )

def classify_mood():
    # Thresholding or some ML model to classify mood based on heart rate and stress
    pass

@app.route('/', methods=['POST'])
def form():
    if request.method == 'POST':
        global HEART_RATE, STRESS

        data = json.loads(request.data)

        # https://developer.samsung.com/sdp/blog/en/2022/05/25/check-which-sensor-you-can-use-in-galaxy-watch-running-wear-os-powered-by-samsung
        HEART_RATE = data['bpm']
        STRESS = data['stress']

        # mood = classify_mood()
        # trigger_alexa(mood)

        return jsonify({'status': 'ok'}), 200

    return jsonify({'status': 'bad input'}), 400

def main():
    app.run(debug=True, port=8080)
    
if __name__ == '__main__':
    main()