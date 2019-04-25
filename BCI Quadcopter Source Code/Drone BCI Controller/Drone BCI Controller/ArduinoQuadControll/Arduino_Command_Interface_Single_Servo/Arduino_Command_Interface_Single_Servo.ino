// This program moves a single servo to pre defined positions using sting commands
// This can be done using putty to comunicate to the arduino. Or arduinos serial interface. 


// Arduino Wiring
// -> Power (RED) to 5V. Ground (BROWN) to GRD/GRC. Signal (YELLOW) to pin 9.
// -> Upload this program to Arduino and connect Servo to board.

// Usage:
// -> Open putty -> Serial -> Com port of arduino -> Open 
// -> Click on terminal
// -> Type the command as show in the if statments 
#include <Servo.h>

Servo servo;
 
int pos = 0;  //Position of servo
String command;
 
void setup() { 
  
  Serial.begin(9600);
  servo.attach(11);  // Attaches the servo on pin 9 to the servo object.
  servo.write(10);  // Resets the position.
} 
 
void loop() {
  
  if (Serial.available()) {  // Returns true if there is serial connection to the arduino.
    
    char received = Serial.read();// Reads input from putty connection 
    command += received; 
    int currentPos = servo.read();//Reads current pos of servo 
    
    if (received == '\n'){
      
      Serial.print("Command: ");
      Serial.print(command);

      if(command == "Climb\n"){
        servo.write(35);
        logServoMove("Climb");
        
       }else if(command == "Hover\n"){
        
        servo.write(27);
        logServoMove("Hover");
        }else if(command == "Land\n"){
          
        servo.write(25);
        logServoMove("Land");
        }else if(command == "Stop\n"){
          
        servo.write(10);
        logServoMove("Stop");
        }else if(command == "Throttle\n" && currentPos + 2 <= 50){
          
        servo.write(currentPos + 2);
        logServoMove("Throttle");
        }else if(command == "Dethrottle\n" && currentPos -2 >= 10){
          
        servo.write(currentPos - 2); 
        logServoMove("Dethrottle");
        }else if (command.indexOf(":") > 0){
        
        int index = command.indexOf(":");
        Serial.println("Index of command" + index);
        command.remove(0, index + 1);//Removes ServoSet: from command to find servo value to set
        int  intValue = command.toInt();

        if(intValue >= 10 && intValue <= 50){
          
          servo.write(intValue);
          logServoMove("ServoSet:" + command );
        }else{
            Serial.println("Value must be within range of 10->50");
          }
       }
      command = ""; // Clear received buffer      
    }      
  } 
}

void logServoMove( String command){
  
    delay(200);          
    Serial.println("Command: " + command);          
    Serial.println(servo.read());
  }
