#Simple class that represents a servo
class Servo:

    def __main__(self):
        self.command = ""
        self.servoPos = 0

    def setServoPos(self, input):
        self.servoPos = input

    def getServoPos(self):
        return self.servoPos

    def setCommand(self, input):
        self.command = input

    def getCommand(self):
        return self.command

