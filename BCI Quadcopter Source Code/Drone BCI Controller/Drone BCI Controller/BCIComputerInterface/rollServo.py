from servo import Servo

#Class represents the servo responsible for controlling the throttle 
class RollServo(Servo):

    def __init__(self, safeValue):
        Servo.__init__(self)
        self.setServoPos(safeValue)

    def stop(self):#Emergency value to stop rolling the quadcopter
        self.setServoPos(35)
        self.setCommand("Stop")
        return self.getServoPos()
    
    def right(self):#Value moves servo so quad rolls to the right   
        self.setServoPos(50)
        self.setCommand("right")
        return self.getServoPos()

    def left(self):#Value moves servo so quad rolls to the left
        self.setServoPos(20)   
        self.setCommand("left")
        return self.getServoPos()

    def setValue(self, value):#Manually set servo pos 
        if(value >= 20 and value <= 50):#Range of values for servo pos to be within
            self.setServoPos(value)
            self.setCommand("SetValue: "+ str(value))
            return self.getServoPos()
        else:
            print("Value: "+ value + " is out of range of 0->70")
