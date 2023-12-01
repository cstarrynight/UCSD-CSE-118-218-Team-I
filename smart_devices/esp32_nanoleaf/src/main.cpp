#include "WiFi.h"
#include "ESPAsyncWebServer.h"
#include <FastLED.h>
#include "secrets.h"

#define NUM_LEDS 60
#define DATA_PIN 6

CRGB leds[NUM_LEDS];
CRGB newColor;
 
AsyncWebServer server(80);

void string2CRGB(String colorString) {
  String colors[3];
  uint8_t p = 0;

  for (uint8_t i = 0; i < colorString.length(); i++) {
    if (colorString[i] == ',') {
      p++;
    } 
    else {
      colors[p] = colors[p] + colorString[i];
    }
  }

  newColor = CRGB(colors[0].toInt(), colors[1].toInt(), colors[2].toInt());
}
 
void setup(){
  Serial.begin(115200);

  // FastLED configure
  FastLED.addLeds<WS2811, DATA_PIN>(leds, NUM_LEDS);
 
  // Connect to Wi-Fi network with SSID and password
  Serial.print("Connecting to ");
  Serial.println(homeSSID);
  WiFi.begin(homeSSID, homePassword);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
 
  Serial.println(WiFi.localIP());
 
  // Webserver routes
  server.on("/lights", HTTP_GET, [](AsyncWebServerRequest *request) {
    String color = request->getParam("color")->value();
    String brightness = request->getParam("brightness")->value();
    String bpm = request->getParam("bpm")->value();

    Serial.println(color);
    Serial.println(brightness);
    Serial.println(bpm);
    Serial.println();

    // Color
    string2CRGB(color);

    // Brightness
    int mappedBrightness = map(brightness.toInt(), 0, 100, 30, 255);
    FastLED.setBrightness(mappedBrightness);
 
    request->send(200);
  });
 
  server.begin();
}
 
void loop() {
  fill_solid(leds, NUM_LEDS, newColor);
  FastLED.show();
}