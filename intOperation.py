"""Module to do all the conversion and calculate the sum of the input"""


from Input import Input                                     #Importing class Input from Input.py
inp = Input()                                               #Creating an instance of class Input

from bitOperation import bitOperation                       #Importing class bitOperation from bitOperation.py
bit = bitOperation()                                        #Creating an instance of class bitOperation
bit.operate()                                               #Calling the function operate() of class bitOperation  

class intOperation:
    def conversion(self):
        self.sumlist = []
        self.intlist = 0
        
        self.sumstr = str(bin(bit.ansAndGate))[2:].zfill(8)         #Slicing is used to cut out 0b of binary conversion and zfill is used to pad strings on the left side of the list with zeros to fill width
        self.sumlist = list(self.sumstr)

        while self.intlist < 8:                                     #While loop is used here to convert string to integer data type to store it in a list
            self.sumlist[self.intlist] = eval(self.sumlist[self.intlist])
            self.intlist = self.intlist + 1
        
        print("\nThe sum in base 10: " ,bit.ansAndGate)
        print("\nThe sum in base 2: " ,self.sumlist)
        
o = intOperation();
o.conversion();
