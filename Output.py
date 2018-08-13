"""Module to ask the user if he wants to run the program again and output the results of the calculation"""

from Input import Input                             #Importing class Input from Input.py
i = Input()                                         #Creating an instance of class Input

from bitOperation import bitOperation               #Importing class bitOperation from bitOperation.py
bit = bitOperation()                                #Creating an instance of class bitOperation

from intOperation import intOperation               #Importing class intOperation from intOperation.py
intOp = intOperation()                              #Creating an instance of class intOperation

import sys
import imp

class Output:
    def final(self):
        while True:                                 #While loop to run the commands over and over again until instructed to quit
            que = input("\nDo you want to run the program again? Type 'y' for Yes and 'n' for No\n")

            if que == 'y' or que == 'Y':            #If statement to check if the user wants to run the program again or not
                imp.reload(sys.modules['Input'])
                imp.reload(sys.modules['bitOperation'])
                imp.reload(sys.modules['intOperation'])
                continue
            elif que == 'n' or que == 'N':
                print("\nThank You")
                break
            else:
                print("Invalid option. Type Y or N")
                continue

out = Output()
out.final()
            
