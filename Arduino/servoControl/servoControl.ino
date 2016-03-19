#include <Servo.h> 

Servo servos[4];

int pos = 0;    // variable to store the servo position 
int delta=1;
int i=0;

void setup() 
{ 
  for(i=0;i<4;i++)
    servos[i].attach(i+6);  // attaches the servo on pin 9 to the servo object 
} 
 
void loop() 
{ 
  pos+=delta;
  if(pos>120) delta=-1;
  else if(pos<60) delta=1;
  

   for(i=0;i<4;i++)
    servos[i].write(pos);
    delay(50);
} 

