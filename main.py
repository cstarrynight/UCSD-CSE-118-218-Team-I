# Import flask application and ngrok python sdk
from server.app import run
from dotenv import load_dotenv
import ngrok, os

load_dotenv()

NGROK_AUTH = os.environ.get('NGROK_AUTH')
NGROK_DOMAIN = os.environ.get('NGROK_DOMAIN')

LOCAL = 8080
ESP32 = '192.168.0.246'

if __name__ == '__main__':
    # Establish connectivity
    listener = ngrok.forward(domain=NGROK_DOMAIN, addr=LOCAL, authtoken=NGROK_AUTH)
    listener_url = listener.url()

    # Output ngrok url to console
    print(' __________________________________________________________________________________________')
    print('|')
    print(f'|  Local forwarding URL established at {listener_url}')
    print('|')
    print(' __________________________________________________________________________________________')
    print('')

    try:
        run(port=LOCAL)
    except KeyboardInterrupt:
        ngrok.disconnect()

    #ngrok config edit
    #ngrok config check