# Import flask application and ngrok python sdk
from server.app import run
from dotenv import load_dotenv
import ngrok, os

load_dotenv()

NGROK_AUTH = os.environ.get('NGROK_AUTH')
NGROK_DOMAIN = os.environ.get('NGROK_DOMAIN')

LOCAL = 8080
ESP32 = 'http://192.168.0.246'

if __name__ == '__main__':
    # Establish connectivity
    listener = ngrok.forward(domain=NGROK_DOMAIN, addr=LOCAL, authtoken=NGROK_AUTH)
    listener_url = listener.url()

    # Output ngrok url to console
    print(' ------------------------------------------------------------------------------------')
    print('|                                                                                    |')
    print(f'|  Local forwarding URL established at {listener_url}  |')
    print('|                                                                                    |')
    print(' ------------------------------------------------------------------------------------')
    print('')

    try:
        run(port=LOCAL, esp32_url=ESP32)

    except KeyboardInterrupt:
        ngrok.disconnect()

    #ngrok config edit
    #ngrok config check