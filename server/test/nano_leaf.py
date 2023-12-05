import requests

red = 66
green = 200
blue = 0

url = f'http://192.168.1.91/color?red={red}&green={green}&blue={blue}'
#url = f'http://192.168.1.91/idle'
url = f'http://192.168.1.91/off'

# Send post request to application form
response = requests.get(url)
print(response)

