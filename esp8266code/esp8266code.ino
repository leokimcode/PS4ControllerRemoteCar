#include <ESP8266WiFi.h>
#include <WiFiUdp.h>
#include <string.h>

int PWMA=5;//Right side
int PWMB=4;//Left side
int DA=0;//Right reverse
int DB=2;//Left reverse
char moveindex;
int pwmVal;
char buffer[3];

const char* ssid = "xxxxx";
const char* password = "xxxxx";
int moveCase = 0;
String pwmString;

WiFiUDP Udp;
unsigned int localUdpPort = 8888;  // local port to listen on
char incomingPacket[255];  // buffer for incoming packets
char  replyPacket[] = "Hi there! Got the message :-)";  // a reply string to send back

void setup() 
{
  Serial.begin(115200);
  pinMode(PWMA, OUTPUT);
  pinMode(PWMB, OUTPUT);
  pinMode(DA, OUTPUT);
  pinMode(DB, OUTPUT);
  Serial.println();
  Serial.printf("Connecting to %s ", ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println(" connected");

  Udp.begin(localUdpPort);
  Serial.printf("Now listening at IP %s, UDP port %d\n", WiFi.localIP().toString().c_str(), localUdpPort);

}

void loop() 
{
  int packetSize = Udp.parsePacket();
  if (packetSize)
  {
    //Serial.printf("Bytes: %d, From: %s, Port: %d\n", packetSize, Udp.remoteIP().toString().c_str(), Udp.remotePort());
    int len = Udp.read(incomingPacket, 255);
    if (len > 0)
    {
      incomingPacket[len] = 0;
    }
    //Serial.printf("%d", len);
    //Serial.printf("UDP packet contents: %s\n", incomingPacket);
    moveindex = incomingPacket[0];
    Serial.printf("%c\n", moveindex);
    for(int i = 0; i<len-1; i++)
    {
      buffer[i] = incomingPacket[i+1];
    }
    pwmVal = (atoi(buffer) - 129) * 255/127;
    Serial.printf("%d\n", pwmVal);

    if(pwmVal<200)
    {
      digitalWrite(PWMA, LOW);
      digitalWrite(PWMB, LOW);
    }
    else
    {

    switch(moveindex)
    {
      case 'b':
        analogWrite(PWMA, pwmVal);
        digitalWrite(DA, HIGH);
        analogWrite(PWMB, pwmVal);
        digitalWrite(DB, HIGH);
        break;

      case 'u':
        analogWrite(PWMA, pwmVal);
        digitalWrite(DA, LOW);
        analogWrite(PWMB, pwmVal);
        digitalWrite(DB, LOW);
        break;

      case 'r':
        analogWrite(PWMA, pwmVal);
        digitalWrite(DA, HIGH);
        analogWrite(PWMB, pwmVal);
        digitalWrite(DB, LOW);
        break;

      case 'l':
        analogWrite(PWMA, pwmVal);
        digitalWrite(DA, LOW);
        analogWrite(PWMB, pwmVal);
        digitalWrite(DB, HIGH);
        break;

       default:
        digitalWrite(PWMA, LOW);
        digitalWrite(PWMB, LOW);
    }
  }
  }
}
