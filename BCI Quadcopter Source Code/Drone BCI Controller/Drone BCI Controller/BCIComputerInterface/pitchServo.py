from servo import Servo

#Class represents the servo responsible for controlling the throttle 
class PitchServo(Servo):
    
    def __init__(self,safeValue):
        self.setServoPos(safeValue)

    def stop(self):#Emergency value to stop rolling the quadcopter
        self.setServoPos(35)
        self.setCommand("Stop")
        return self.getServoPos()


    def forward(self):#Value moves servo so quad rolls to the right   
        self.setServoPos(10)
        self.setCommand("forward")
        return self.getServoPos()

    def backward(self):#Value moves servo so quad rolls to the left
        self.setServoPos(50)
        self.setCommand("backward")
        value = self.getServoPos()
        return value 

    def setValue(self, value):#Manually set servo pos 
        if(value >= 10 and value <= 50):#Range of values for servo pos to be within
            self.setServoPos(value)
            self.setCommand("SetValue: "+ str(value))
            return self.getServoPos()
        else:
            print("Value: "+ value + " is out of range of 0->70")
      

