// This program moves a single servo to pre defined positions using keyboard inputs
// This can be done using putty to comunicate to the arduino. Or arduinos serial interface. 
// This keyboard control can directly controll the quadcopters throttle 


// Arduino Wiring
// -> Power (RED) to 5V. Ground (BROWN) to GRD/GRC. Signal (YELLOW) to pin 9.
// -> Upload this program to Arduino and connect Servo to board.

// Usage:
// -> Open putty -> Serial -> Com port of arduino -> Open 
// -> Click on terminal
// -> Press 'a' to move servo to climb
// -> Press 'd' to move servo to hover
// -> Press 's' to move servo to land
// -> Press 'f' to move servo to stop moving
#include <Servo.h>

Servo servo;
 
int pos = 0;  //Position of servo
 
void setup() { 
  
  Serial.begin(9600);
  servo.attach(9);  // Attaches the servo on pin 9 to the servo object.
  servo.write(10);  // Resets the position.
} 
 
void loop() {
  
  if (Serial.available()) {  // Returns true if there is serial connection to the arduino.

    char ch = Serial.read();// Reads input from putty connection 
    int currentPos = servo.read();//Reads current pos of servo 

    switch(ch){
      case 'a':
        servo.write(35);// Climb
        logServoMove();
        break;  

      case 's':
        servo.write(27);// Hover
        logServoMove();
        break;

      case 'd':
        servo.write(25);// Land
        logServoMove();
        break;

      case 'f':
        servo.write(10);// 0 Throttle
        logServoMove();
        break;

      case 'j':// Increments throttle
        if(currentPos + 2 <= 50){

          servo.write(currentPos + 2);
          logServoMove();
        }
        break;

      case 'k':// Decrements throttle
        if(currentPos - 2 >= 10){

          servo.write(currentPos - 2);
          logServoMove();
        }
        break;
      default:
        //
        break;
    }
  } 
}

void logServoMove(){
  
    delay(5);                       
    Serial.print(servo.read());
    Serial.println();
  }
