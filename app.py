from flask import Flask, request, jsonify
import json 

app = Flask(__name__)

@app.route('/', methods=['POST'])
def form():
    if request.method == 'POST':
        data = json.loads(request.data)

        # https://developer.samsung.com/sdp/blog/en/2022/05/25/check-which-sensor-you-can-use-in-galaxy-watch-running-wear-os-powered-by-samsung
        ppg = data['bpm']
        stress = data['stress']

        return jsonify({'status': 'ok'}), 200

    return jsonify({'status': 'bad input'}), 400

def main():
    app.run(debug=True, port=8080)
    
if __name__ == '__main__':
    main()