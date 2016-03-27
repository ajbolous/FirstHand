#include <Servo.h>


Servo servos[4];

int pos = 0;    // variable to store the servo position
int delta = 1;
int i = 0;
byte c;
int count = 0;
byte buff[8] = {100, 100, 100, 100, 100, 100, 100, 100};

void setup()
{
  Serial.begin(9600);
  for (i = 0; i < 4; i++)
    servos[i].attach(i + 2); // attaches the servo on pin 9 to the servo object
}

void loop()
{
  if (Serial.available()) {
    c = Serial.read();
    for (i = 0; i < 7; i++) {
      buff[i] = buff[i + 1];
    }
    buff[7] = c;
    if (buff[0] == 200 && buff[1] == 200 && buff[6] == 200 && buff[7] == 200) {
      Serial.println("got " + String(buff[2]) + "," +  String(buff[3]) + "," +  String(buff[4]) + "," +  String(buff[5]));
      for (i = 0; i < 4; i++) {
        servos[i].write(buff[2 + i]);
      }
    }
  }
}

