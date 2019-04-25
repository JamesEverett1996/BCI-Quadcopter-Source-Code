// Simple demo to get commands working from serial comunication to uno
#include <Servo.h>

Servo servo;
 
int pos = 0;  //Position of servo
String command;
 
void setup() { 
  
  Serial.begin(9600);
  servo.attach(9);  // Attaches the servo on pin 9 to the servo object.
  servo.write(10);  // Resets the position.
} 
 
void loop() {
    if(Serial.available()){
        char recieved = Serial.read();
        command += recieved; 

        // Process message when new line character is recieved
        if (recieved == '\n')
        {
            Serial.print("Command: ");
            Serial.print(command);

            if(command == "Throttle\n"){
              servo.write(180);
              Serial.println("Throttle");
              delay(15);
              
            }else if(command == "Land\n"){
              servo.write(0);
              Serial.println("Land");
              delay(15);
            }
            command = ""; // Clear recieved buffer
        }
    }
}
