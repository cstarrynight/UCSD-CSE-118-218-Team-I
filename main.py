# Import flask application and ngrok python sdk
from server.app import run
import ngrok

LOCAL = 8080
ESP32 = '192.168.0.246'

if __name__ == '__main__':
    # Establish connectivity
    listener = ngrok.forward(domain='gnu-pleased-seriously.ngrok-free.app', addr=LOCAL, authtoken='2WPebJnja7EON792v2sEh5dixck_5bqbGZ16igmNq5oMp6Rau')
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