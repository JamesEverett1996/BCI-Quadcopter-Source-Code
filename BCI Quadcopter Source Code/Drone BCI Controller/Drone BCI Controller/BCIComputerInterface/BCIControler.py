import sys
import os
import keyboard
import threading
import multiprocessing
import time
import logging
import msvcrt

from arduinoShieldInterface import ArduinoShieldInterface 

""" 
21/02/2019 James Everett
This file acts as a keyboard controller that maps keys to commands.
It has sepperate threads to listen for throttle, roll comands and kill switch commands

Intructions
-----------
Press 'esc'   -> Stop throttle of quad and reset roll 
Press 'w'     -> Increases throttle 
Press 'space' -> Decreases throttle
Press 'up'    -> Roll quadcopter forward
Press 'down'  -> Roll quadcopter backward
Press 'right' -> Roll quadcotper right
Press 'left'  -> Roll quadcotper leftwww      www                                                                                                      
"""

logging.basicConfig(filename='BCILog.log',level=logging.DEBUG, format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(funcName)s - line %(lineno)d")

class BCIController: 

    def __init__(self, com, rate):

        print("Setting Up Controller")
        self.arduinoInterface = ArduinoShieldInterface(com, rate)
        self.emoKeyCommand = ""
        self.quitPress = False

    # Function acts as a controller that alters throttle from keyboard inputs
    def throttleKeyboardControll(self):

        while True:
            try: 
                while keyboard.is_pressed('w'):# While W is pressed throttle is inceased every 0.1 s
                    print("Increasing Throttle: W")
                    logging.info("W Pressed Increasing throttle")
                    self.arduinoInterface.throttle()
                    time.sleep(0.1)#Delays the pringing of w
                        
                while keyboard.is_pressed('space'):# While space is pressed throttle is decreased every 0.1 s 
                    print("Decreasing Throttle: space")
                    logging.info("Space Pressed decreasing throttle")
                    self.arduinoInterface.dethrottle()
                    time.sleep(0.1)
                
                if( self.quitPress == True):
                    break
            except:
                error = sys.exc_info()
                print("Error: throttleKeyboardControll ", error) 
                logging.error("Error: throttleKeyboardControll " + error)
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
                        print("Forwards: up")
                        logging.info("Up Pressed rolling forward")
                        self.arduinoInterface.resetAngle()
                        self.arduinoInterface.forward()
                        keyPress = True
                        upPress = True

                elif keyboard.is_pressed('down'):# Rolls quad backwards if arrow key is pressed down
                    if not downPress:
                        print("Backwards: down")
                        logging.info("Down Pressed rolling backwards")
                        self.arduinoInterface.resetAngle()
                        self.arduinoInterface.backward()
                        keyPress = True
                        downPress = True

                elif keyboard.is_pressed('left'):# Quad rolls left
                    if not leftPress:
                        print("Roll Left: Left")
                        logging.info("Left Pressed rolling left")
                        self.arduinoInterface.resetAngle()
                        self.arduinoInterface.left()
                        keyPress = True
                        leftPress = True

                elif keyboard.is_pressed('right'):# Quad rolls right
                    if not rightPress:
                        print("Roll Right: Right")
                        logging.info("Right Pressed rolling right")
                        self.arduinoInterface.resetAngle()
                        self.arduinoInterface.right()
                        keyPress = True
                        rightPress = True
                
                elif keyPress == True:
                    self.arduinoInterface.resetAngle()
                    keyPress = False
                
                elif( self.quitPress== True):
                    break

                else:
                    upPress = False
                    downPress = False
                    leftPress = False
                    rightPress = False
            except:
                error = sys.exc_info()
                print("Error: rollKeyboardControll ", error)
                logging.error("Error: rollKeyboardControll " + error)

                break
            time.sleep(0.1)

    # Function acts as a controller kill switch when esc is pressed
    def killSwitchKeyboardControll(self):

        escPress = False

        while True:
            try:
                if keyboard.is_pressed('esc'):
                    if not escPress:# When esc is pressed quads roll is reset to 0 and throttle is rest to 0
                        print("Esc Pressed quad killswitch activated")
                        logging.info("Esc Pressed quad killswitch activated")
                        self.arduinoInterface.killThrottle()
                        self.arduinoInterface.resetAngle()
                        escPress = True

                elif keyboard.is_pressed('q'):
                    if not self.quitPress:
                        print("Quitting Q Pressed")
                        logging.info("Quitting BCIController Q Pressed")
                        self.arduinoInterface.killThrottle()
                        self.arduinoInterface.resetAngle()
                        self.quitPress = True
                        os._exit(1)
                        break

                else:
                    escPress = False
            except:
                error = sys.exc_info()
                print("Error: KillSwitchKeyboard ", error)
                logging.error("Error: KillSwitchKeyboard " + error)
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
                    throttleValue = 38
                    print("Increase Altitude EmoKecommandCommand: Throttle ", throttleValue, "\n")
                    print("FORWARD")
                    logging.info("Increase Altitude EmoKecommandCommand: Throttle ")
                    self.arduinoInterface.setThrottle(throttleValue)
                elif(command == 'h'):
                    throttleValue = 25
                    print("Backwards EmoKecommandCommand: Throttle ", throttleValue, "\n")
                    print("HOVER")
                    logging.info("Increase Altitude EmoKecommandCommand: Throttle ")
                    self.arduinoInterface.setThrottle(throttleValue)
                elif(command == 'l'):
                    throttleValue = 20
                    print("Left EmoKecommandCommand: Throttle ", throttleValue, "\n")
                    print("LAND")
                    logging.info("Increase Altitude EmoKecommandCommand: Throttle ")
                    self.arduinoInterface.setThrottle(throttleValue)
                elif(keyboard.is_pressed('q') or command == 'q' or self.quitPress == True): 
                    throttleValue = 10
                    print("Throttle Value ", throttleValue)
                    print("Quitting Application")
                    logging.info("Quitting")
                    self.arduinoInterface.setThrottle(throttleValue)
                    os._exit(1)
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

    controller = BCIController('COM6', 9600)
    controller.run()


