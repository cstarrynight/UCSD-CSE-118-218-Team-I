import requests
import time
import numpy as np
import pandas as pd
import os

URL = 'https://localhost:8080'
LENGTH = 60
DELAY = 1

np.random.seed(1)

def spoof_data(path):
    bpm_data = sorted(np.random.normal(loc=70, scale=20, size=LENGTH))
    stress_data = sorted(np.random.normal(loc=80, scale=1, size=LENGTH))

    data = {'bpm': bpm_data, 'stress': stress_data}
    data = pd.DataFrame(data)

    data.to_csv(path, index=False)

if __name__ == '__main__':
    path = f'{os.path.join(os.path.dirname(__file__))}/spoof_data.csv'
    spoof_data(path)

    data = pd.read_csv(path)

    for index, row in data.iterrows():
        row = dict(row)
        requests.post(NGROK_URL, json=row)
        time.sleep(DELAY)

        print(row)