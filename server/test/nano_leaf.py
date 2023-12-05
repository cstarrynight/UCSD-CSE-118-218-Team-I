import requests

red = 66
green = 200
blue = 0

#url = f'http://192.168.1.91/color?red={red}&green={green}&blue={blue}'
#url = f'http://192.168.1.91/idle'
url = 'https://3b26-69-196-34-63.ngrok-free.app/off'

#url = f'https://172.20.10.3/color?red={red}&green={green}&blue={blue}'

#url = f'https://c1af-69-196-44-88.ngrok-free.app/color?red={red}&green={green}&blue={blue}'

# Send post request to application form
response = requests.get(url)
print(response)

#https://3b26-69-196-34-63.ngrok-free.app

