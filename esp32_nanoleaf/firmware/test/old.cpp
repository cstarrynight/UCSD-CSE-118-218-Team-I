// Load Wi-Fi library
#include <WiFi.h>

// Replace with your network credentials
const char* ssid = "Nguyen_family24";
const char* password = "5648936kng24";

// Set web server port number to 80
WiFiServer server(80);

// Variable to store the HTTP request
String header;

void setup() {
  Serial.begin(115200);

  // Connect to Wi-Fi network with SSID and password
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  // Print local IP address and start web server
  Serial.println("");
  Serial.println("WiFi connected.");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  server.begin();
}

void loop(){
  WiFiClient client = server.available();   // Listen for incoming clients

  if (client) {
    String currentLine = "";

    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
        Serial.write(c);
        header += c;

        if (c == '\n') {                    
          // If the byte is a newline character, that's the end of the client HTTP request, so send a response:
          if (currentLine.length() == 0) {
            // HTTP headers always start with a response code (e.g. HTTP/1.1 200 OK)
            // and a content-type so the client knows what's coming, then a blank line:
            client.println("HTTP/1.1 200 OK");
            client.println();

            Serial.println(header.in);
            
            // turns the GPIOs on and off
            if (header.indexOf("GET /test") >= 0) {
              Serial.println("GPIO 26 on");
            }

            // The HTTP response ends with another blank line
            client.println();

            // Break out of the while loop
            break;
          }
          else {
            currentLine = "";
          }
        }
        else if (c != '\r') {     // if you got anything else but a carriage return character,
          currentLine += c;       // add it to the end of the currentLine
        }
      }
    }
    // Clear the header variable
    header = "";

    // Close the connection
    client.stop();
    Serial.println("Client disconnected.");
    Serial.println("");
  }

}