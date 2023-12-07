# Import flask application and ngrok python sdk
from server.app import run
import ngrok

LOCAL = 8080
ESP32 = '192.168.0.246'

if __name__ == '__main__':
    # Establish connectivity
    local_listener = ngrok.forward(addr=LOCAL, authtoken_from_env=True)

    # Output ngrok url to console
    print(f'Local forwarding URL established at {local_listener.url()}')

    run(port=LOCAL)

    #ngrok.disconnect()