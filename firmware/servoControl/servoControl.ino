#include <Servo.h>


Servo servos[4];

int pos = 0;    // variable to store the servo position
int delta = 1;
int i = 0;

void setup()
{
  Serial.begin(9600);
  for (i = 0; i < 4; i++)
    servos[i].attach(i + 2); // attaches the servo on pin 9 to the servo object
}
char c;
int count = 0;
void loop()
{
  if (Serial.available()) {
    c = Serial.read();
        if (c == 0)
          count++;

    if (count == 2) {
      for (int i = 0; i < 4; i++) {
        c = Serial.read();
        servos[i].write(c);
        Serial.println("got angle : " + String(c));
      }
      count=0;
    }
  }
}

