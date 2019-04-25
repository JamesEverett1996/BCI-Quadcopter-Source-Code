import serial
import time
from arduinoServoInterface import ArduinoServoInterface
from throttleServo import ThrottleServo
from rollServo import RollServo
from pitchServo import PitchServo

"""
23/01/2019
This class acts as a simple interface between Python scripts and the aurdino that controlls the servors which operate the quadcopters controller. 
It creates a serial link to the Arduino so the the servos can be commanded. 
"""
class ArduinoShieldInterface:

    def __init__(self, comPort,  baudRate):
        print("Setting up Controller")
        self.servoInterface = ArduinoServoInterface(comPort,  baudRate)
        self.throttleServo = ThrottleServo(10)
        self.rollServo = RollServo(35)
        self.pitchServo = PitchServo(35)

        #Move servo to zero input values// Values where controller does not move quadcopter
        self.servoInterface.servoSet(1, 10)
        self.servoInterface.servoSet(2, 35)
        self.servoInterface.servoSet(3, 35)

    def throttle(self):
        self.servoInterface.servoSet(1, self.throttleServo.throttle())
    
    def dethrottle(self):
        self.servoInterface.servoSet(1, self.throttleServo.dethrottle())

    def setThrottle(self, pos):
        self.servoInterface.servoSet(1, self.throttleServo.setThrottle(pos))

    def killThrottle(self):
        self.servoInterface.servoSet(1, self.throttleServo.stop())
    
    def forward(self):
        self.servoInterface.servoSet(2, self.pitchServo.forward())
    
    def backward(self):
        self.servoInterface.servoSet(2, self.pitchServo.backward())
    
    def pitchStop(self):
        self.servoInterface.servoSet(2, self.pitchServo.stop())

    def left(self):
        self.servoInterface.servoSet(3, self.rollServo.left())
    
    def right(self):
        self.servoInterface.servoSet(3, self.rollServo.right())
    
    def rollStop(self):
        self.servoInterface.servoSet(3, self.rollServo.stop())

    def resetAngle(self):
        self.rollStop() 
        self.pitchStop()


#Test Code
"""
print("Test Ardino ShieldInterface")
test = ArduinoShieldInterface('COM6',9600)
print("Interface Has been created")
time.sleep(1)
test.setThrottle(30)
print("f")
time.sleep(1)
test.setThrottle(10)
print("d")
time.sleep(1)
test.setThrottle(20)
print("s")
time.sleep(1)
test.setThrottle(40)
print("a")"""
#test.pitchStop()
#time.sleep(1)
#print("Backward")
#test.backward()
#time.sleep(1)
#print("Forward")
#test.forward()
#time.sleep(1)
#print("PirchStop")
#test.pitchStop()
#test.right()
#time.sleep(1)
#test.rollStop()
#time.sleep(1)
#test.left()
#test.rollStop()
"""time.sleep(0.2)
test.resetAngle()

time.sleep(5)

test.left()
time.sleep(0.2)
#test.rollStop()
time.sleep(0.2)
test.right()
time.sleep(0.2)
test.resetAngle()
"


for x in range(4):
    test.throttle()
    time.sleep(0.2)

for x in range(4):
    test.dethrottle()
    time.sleep(0.2)

for x in range(4):
    test.throttle()
    time.sleep(0.2)

test.killThrottle()

"""
