import keyboard
import threading
import multiprocessing
import time
import sys
import msvcrt

# 04/04/2019 James Everett
# This script is used for developing and testing the logic of the controller interface

class ControllerDemo : 

    def __init__(self, com, rate):
        print("Setting Up Dummy Controller")
        self.emoKeyCommand = ""
        self.quitPress = False

    # Function acts as a controller that alters throttle from keyboard inputs
    def throttleKeyboardControll(self):

        while True:
            try: 
                while keyboard.is_pressed('w'):# While W is pressed throttle is inceased every 0.1 s
                    print("W")
                    time.sleep(0.1)#Delays the pringing of w

                while keyboard.is_pressed('space'):# While space is pressed throttle is decreased every 0.1 s 
                    print("space")
                    time.sleep(0.1)
                
                if( self.quitPress == True):
                    break
            except:
                print("Error: throttleKeyboardControll ", sys.exc_info()) 
            time.sleep(0.1)
            

    # Function acts as a controller that alters quads roll from keyboard inputs  
    def rollKeyboardControll(self):

        keyPress = False
        upPress = False
        downPress = False
        leftPress = False
        rightPress = False

        while True:
            try: 
                if keyboard.is_pressed('up'):
                    if not upPress:# Rolls quad forward if up arrow key is pressed up
                        print("up")
                        keyPress = True
                        upPress = True

                elif keyboard.is_pressed('down'):# Rolls quad backwards if arrow key is pressed down
                    if not downPress:
                        print("down")
                        keyPress = True
                        downPress = True

                elif keyboard.is_pressed('left'):# Quad rolls left
                    if not leftPress:
                        print("left")
                        keyPress = True
                        leftPress = True

                elif keyboard.is_pressed('right'):# Quad rolls right
                    if not rightPress:
                        print("right")
                        keyPress = True
                        rightPress = True
                
                elif keyPress == True:
                    keyPress = False
                
                elif( self.quitPress== True):
                    break

                else:
                    upPress = False
                    downPress = False
                    leftPress = False
                    rightPress = False
            except:
                print("Error: rollKeyboardControll ", sys.exc_info())
                break
            time.sleep(0.1)

    # Function acts as a controller kill switch when esc is pressed
    def killSwitchKeyboardControll(self):

        escPress = False

        while True:
            try:
                if keyboard.is_pressed('esc'):
                    if not escPress:# When esc is pressed quads roll is reset to 0 and throttle is rest to 0
                        print("esc")
                        escPress = True

                elif keyboard.is_pressed('q'):
                    if not self.quitPress:
                        print("Quiting Q Pressed")
                        self.quitPress = True
                        #sys.exit(0)
                        break

                else:
                    escPress = False
            except:
                print("Error: KillsSwitchKeyboard ", sys.exc_info())
                break
            time.sleep(0.1)

    # Reads commands from emokey interface when application 
    def readEmoKeyCommand(self):

        while True:
            try: 
                commandHex = msvcrt.getch()
                command  = str(commandHex, 'utf-8')
                print("EmoKeyCommand " + command)

                if(command == 't'):
                    throttleValue = 40
                    print("Increase Altitude EmoKecommandCommand: Throttle ", throttleValue, "\n")
                    print("FORWARD")
                elif(command == 'h'):
                    throttleValue = 35
                    print("Backwards EmoKecommandCommand: Throttle ", throttleValue, "\n")
                    print("HOVER")
                elif(command == 'l'):
                    throttleValue = 20
                    print("Left EmoKecommandCommand: Throttle ", throttleValue, "\n")
                    print("LAND")
                elif(keyboard.is_pressed('q') or command == 'q' or self.quitPress == True): 
                    throttleValue = 0
                    print("Throttle Value ", throttleValue)
                    print("Quitting Application")
                    break 
            except:
                print("Error: readEmoKeycommand ", sys.exc_info())
                break
            time.sleep(0.1)
 
    def run(self):
        
        t1 = threading.Thread(target = self.killSwitchKeyboardControll)
        t2 = threading.Thread(target = self.throttleKeyboardControll)
        t3 = threading.Thread(target = self.rollKeyboardControll)
        t4 = threading.Thread(target = self.readEmoKeyCommand)

        print("\n#################################################################################################################################################################################")
        print("#################################################################################################################################################################################")
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print("Finished set up\n") 
        string = """\
                   _____                .__  .__               __  .__                __________                   .___      
                  /  _  \ ______ ______ |  | |__| ____ _____ _/  |_|__| ____   ____   \______   \ ____ _____     __| _/__.__.
                 /  /_\  \\____ \\____ \|  | |  |/ ___\\__  \\   __\  |/  _ \ /    \   |       _// __ \\__  \   / __ <   |  |
                /    |    \  |_> >  |_> >  |_|  \  \___ / __ \|  | |  (  <_> )   |  \  |    |   \  ___/ / __ \_/ /_/ |\___  |
                \____|__  /   __/|   __/|____/__|\___  >____  /__| |__|\____/|___|  /  |____|_  /\___  >____  /\____ |/ ____|
                        \/|__|   |__|                \/     \/                    \/          \/     \/     \/      \/\/      
            
            
                """
        print(string, "\n\n\n")  

        t1.start()
        t2.start()
        t3.start()
        t4.start()

        t1.join()
        t2.join()
        t3.join()
        t4.join()

if __name__ == '__main__':

    controller = ControllerDemo('C ControllerDemoOM3', 9600)
    controller.run()


