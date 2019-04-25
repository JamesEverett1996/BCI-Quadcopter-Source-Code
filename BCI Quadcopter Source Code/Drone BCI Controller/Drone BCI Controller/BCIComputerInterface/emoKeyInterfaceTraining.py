import sys 
import time
import keyboard
import msvcrt

"""
04/04/2019 James Everett
The emoKecommand application cannot enter commands to applications onlcommand write strings to applications,
This code when run from the command line reads evercommand char written to the cmd line.
This allows the emoKecommand application to interface with a commandline. 
"""
while True:

    throttleValue = 0
    try :
        x = msvcrt.getch()
        command  = str(x, 'utf-8')
        
        if(command == 't'):
            throttleValue = 30
            print("Increase Altitude EmoKecommandCommand: Throttle ", throttleValue, "\n")
            print("FORWARD")
        elif(command == 'h'):
            throttleValue = 25
            print("Backwards EmoKecommandCommand: Throttle ", throttleValue, "\n")
            print("HOVER")
        elif(command == 'l'):
            throttleValue = 20
            print("Left EmoKecommandCommand: Throttle ", throttleValue, "\n")
            print("LAND")
        elif(keyboard.is_pressed('q') or command == 'q'): 
            throttleValue = 10
            print("Throttle Value ", throttleValue)
            print("Quitting emoKeyInterface.py")
            break
    except:
        print("Error: ", sys.exc_info())
   