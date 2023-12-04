#include <Arduino.h>
#include <esp_task_wdt.h>

#include "WiFi.h"
#include "ESPAsyncWebServer.h"

#include "secrets.h"

#define RED_PIN 23
#define GREEN_PIN 22
#define BLUE_PIN 21

#define WATCHDOG_TIMEOUT_S 30

bool idle = true;
int red = 0, green = 0, blue = 0;
int counter = 1;
 
AsyncWebServer server(80);

void setColor(int redValue, int greenValue, int blueValue) {
  analogWrite(RED_PIN, redValue);
  analogWrite(GREEN_PIN, greenValue);
  analogWrite(BLUE_PIN, blueValue);
}
 
void setup(){
  Serial.begin(115200);
  esp_task_wdt_init(WATCHDOG_TIMEOUT_S, false);

  // Led strips setup
  pinMode(RED_PIN, OUTPUT);
  pinMode(GREEN_PIN, OUTPUT);
  pinMode(BLUE_PIN, OUTPUT);
 
  // Connect to Wi-Fi network with SSID and password
  Serial.print("Connecting to ");
  Serial.println(mesaSSID);
  WiFi.begin(mesaSSID, mesaPassword);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
 
  Serial.println(WiFi.localIP());
 
  // Webserver routes
  server.on("/color", HTTP_GET, [](AsyncWebServerRequest *request) {
    int requestedRed = request->getParam("red")->value().toInt();
    int requestedGreen = request->getParam("green")->value().toInt();
    int requestedBlue = request->getParam("blue")->value().toInt();

    if ((requestedRed >= 0 && requestedRed <= 255) &&
        (requestedGreen >= 0 && requestedGreen <= 255) &&
        (requestedBlue >= 0 && requestedBlue <= 255)) {
          red = requestedRed;
          green = requestedGreen;
          blue = requestedBlue;

          idle = false;
        }
    
    Serial.println("RGB=(" + String(red) + ", " + String(green) + ", "  + String(blue) + ")");
    Serial.println();
 
    request->send(200);
  });

  // Webserver routes
  server.on("/idle", HTTP_GET, [](AsyncWebServerRequest *request) {
    red = green = blue = 0;
    idle = true;
    counter = 1;
 
    request->send(200);
  });

  // Webserver routes
  server.on("/off", HTTP_GET, [](AsyncWebServerRequest *request) {
    red = green = blue = 0;
    idle = false;
 
    request->send(200);
  });
 
  server.begin();
}
 
void loop() {
  if (idle) {
    // Do fade protocol
    if (red < 5 || green < 5 || blue < 5) {
      red = green = blue = 5;
      counter = 1;
    }
    else if (red > 150 || green > 150 || blue > 150) {
      red = green = blue = 150;
      counter = -1;
    }

    red = red + counter;
    green = green + counter;
    blue = blue + counter;

    delay(10);
  }

  setColor(red, green, blue);

}