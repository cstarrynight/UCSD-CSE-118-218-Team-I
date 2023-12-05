import requests
import csv
import time
import numpy as np
import pandas as pd
import os

NGROK_URL = ''
LENGTH = 60
DELAY = 1

np.random.seed(1)

def spoof_data():
    bpm_data = sorted(np.random.normal(loc=70, scale=20, size=LENGTH))
    stress_data = sorted(np.random.normal(loc=80, scale=1, size=LENGTH))

    data = {'bpm': bpm_data, 'stress': stress_data}
    data = pd.DataFrame(data)

    path = f'{os.path.join(os.path.dirname(__file__))}/spoof_data.csv'
    data.to_csv(path, index=False)

if __name__ == '__main__':
    spoof_data()

    path = f'{os.path.join(os.path.dirname(__file__))}/spoof_data.csv'
    data = pd.read_csv(path)

    for index, row in data.iterrows():
        row = dict(row)
        requests.post(NGROK_URL, json=row)
        time.sleep(DELAY)

        print(row)