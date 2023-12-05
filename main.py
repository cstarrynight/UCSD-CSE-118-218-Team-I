# Import flask application and ngrok python sdk
from server.app import run
import ngrok

LOCAL = 8080
ESP32 = '172.20.10.3'

if __name__ == '__main__':
    # Establish connectivity
    local_listener = ngrok.forward(addr=LOCAL, authtoken_from_env=True)
    esp32_listener = ngrok.forward(addr=ESP32, authtoken_from_env=True)

    # Output ngrok url to console
    print(f'Local forwarding URL established at {local_listener.url()}')
    print(f'ESP32 forwarding URL established at {esp32_listener.url()}')

    run(port=LOCAL, esp32_url=esp32_listener.url())

    #ngrok.disconnect()