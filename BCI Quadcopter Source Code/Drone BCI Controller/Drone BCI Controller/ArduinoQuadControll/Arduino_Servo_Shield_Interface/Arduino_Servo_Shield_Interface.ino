//This File acts as a interface between the computer and servo controll on the arduino. 
#include <Servo.h>

Servo throttleServo;
Servo pitchServo;
Servo rollServo;

String command;
 
void setup() { 
  
  Serial.begin(9600);
  
  throttleServo.attach(10);//Servo :Throttle attached at pin 10
  throttleServo.write(10);
  delay(39);
  
  pitchServo.attach(11);//Servo: Roll Forwards and backwards at pin 11
  pitchServo.write(35);  
  delay(39);
  
  rollServo.attach(12);//Servo: Roll Left and Right at pin 12
  rollServo.write(35);
  delay(39);
} 
 
void loop() {
  
  if (Serial.available()) {  // Returns true if there is serial connection to the arduino.
    
    char received = Serial.read();// Reads input from putty connection 
    command += received;
    
    if (received == '\n'){
      

      if(command.indexOf("1:") > 0){

        int index = command.indexOf("1:");
        String stringValue = command;
        stringValue.remove(0, index + 2);//Removes ServoSet: from command to find servo value to set
        int  intValue = stringValue.toInt();
        
        int throttlePos = throttleServo.read();
        moveServo(throttleServo, throttlePos, intValue);
        logServoMove(command, throttleServo, intValue);
      }else if(command.indexOf("2:") > 0){

        int index = command.indexOf("2:");
        String stringValue = command;
        stringValue.remove(0, index + 2);//Removes ServoSet: from command to find servo value to set
        int  intValue = stringValue.toInt();

        int pitchPos = pitchServo.read();
        moveServo(pitchServo, pitchPos, intValue);
        logServoMove(command, pitchServo, intValue);
      }else if(command.indexOf("3:") > 0 ){

        int index = command.indexOf("3:");
        String stringValue = command;
        stringValue.remove(0, index + 2);//Removes ServoSet: from command to find servo value to set
        int  intValue = stringValue.toInt();

        int rollPos = rollServo.read();
        moveServo(rollServo, rollPos, intValue);
        logServoMove(command, rollServo, intValue);
      }
      command = ""; // Clear received buffer www      
    }       
  }      
} 



void logServoMove( String command, Servo servo, int pos){
  
    delay(39);               
    
    if(pos == servo.read()){//Checks to see if servo moves correctly

      Serial.write("ServoMovePass\n");//Ack packet to be sent back
    }else{
      Serial.write("ServoMoveFail\n");//Fail packet to be sent back
    }
  }
  
  void moveServo(Servo servo , int currentPos, int targetPos){

    if(currentPos <= targetPos){
      for(int x = currentPos; x <= targetPos; x +=1 ){
        servo.write(x);
        delay(5);  
      
      }
    }else if(targetPos<= currentPos){
  
      for(int x = currentPos; x >= targetPos; x -=1 ){
        servo.write(x);
        delay(5);  
    }
  }
}
