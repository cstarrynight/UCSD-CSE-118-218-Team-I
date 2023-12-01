import requests

url = 'http://192.168.0.71/lights?color=0,255,64&brightness=70'

# Send post request to application form
response = requests.get(url)
print(response)

