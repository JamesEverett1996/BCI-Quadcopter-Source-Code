from servo import Servo

#Class represents the servo responsible for controlling the throttle 
class ThrottleServo(Servo):

    def __init__(self, safeValue):
        Servo.__init__(self)
        self.setServoPos(safeValue)

    def stop(self):#Emergency button that puts throttle to 0
        self.setServoPos(10)
        self.setCommand("Stop")
        return self.getServoPos()

    def throttle(self):#When this function is used throttle servo pos is incremented by 2
        
        currentPos = self.getServoPos()
        print("ThrottleServo Position : " + str(currentPos))

        if( currentPos < 50):
            self.setServoPos(currentPos + 5)
            self.setCommand("Power")
        else:
            print("Already max throttle")
        return self.getServoPos()

    def dethrottle(self):#When this function is used throttle servo pos is decremented by 2
      
        currentPos = self.getServoPos()
        print("ThrottleServo Position: " + str(currentPos))
        
        if(currentPos > 10 ):
            self.setServoPos(currentPos - 5)
            self.setCommand("Power")
        else: 
            print("Already min throttle")
        return self.getServoPos()
    
    def setThrottle(self, throttleValue):
        if(throttleValue <= 50 and throttleValue >= 10):
            self.setServoPos(throttleValue)
            self.setCommand("Power")
        else:
            print("Throttle Value is not in range of 50 -10 ")
        return self.getServoPos() 


    
    

