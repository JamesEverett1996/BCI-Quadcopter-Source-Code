import serial
import time
import logging
import sys

"""
23/01/2019 James Everett
This class acts as a simple interface between Python scripts and the aurdino that controlls the servors which operate the quadcopters controller. 
It creates a serial link to the Arduino so the the servos can be commanded and verified. 
"""

logging.basicConfig(filename='BCILog.log',level=logging.DEBUG, format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(funcName)s - line %(lineno)d")

class ArduinoServoInterface:

    def __init__(self, comPort, baudRate):
        try:
            self.arduino = serial.Serial(comPort, baudRate, timeout = 1)
            time.sleep(1)#When a serial link is opened the arduino needs time to reset to process commands. 
            logging.info("Serial Link to arduino created")
        except:
            error = sys.exc_info()
            print("Error connecting to arduino ", error)
            logging.error("Error connecting to arduino" + error)

    def logCommand(self, command):
        time.sleep(0.1)
        response = str( self.arduino.readline())
        logging.info("Command: " + command)
        logging.info("Response: " + response)

    def servoSet(self, servoNum, servoValue):#Sets servo position 
        commandString = "ServoSet" + str(servoNum) + ":" + str(servoValue) + "\n"
        logging.info("Command: " + commandString)
        self.arduino.write(commandString.encode())
        self.logCommand("ServoSet" + str(servoNum) + ":" + str(servoValue))

    def closeSerialLink(self):
        self.arduino.close()
        logging.info("Closing Serial Link")

#Test code
"""
test = ArduinoServoInterface('COM6',9600)
test.servoSet(1,90)
time.sleep(0.2)
test.servoSet(1,60)
time.sleep(0.2)
test.servoSet(2,0)
time.sleep(0.2)
test.servoSet(2,90)
time.sleep(0.2)
test.servoSet(3,0)
time.sleep(0.2)
test.servoSet(3,90)"""
