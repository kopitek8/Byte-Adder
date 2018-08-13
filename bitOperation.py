"""Module to do all the bit operations"""


from Input import Input                                 #Importing class Input from Input.py
i = Input()                                             #Creating an instane of class Input
i.userInput()                                           #Calling the userInput() function of class Input

class bitOperation:
    def operate(self):                                  #The function operate() takes a parameter self so that when an instance is created of a class, the variables can be called by the instance
        self.carry = 1

        
        self.xorGate = i.a ^ i.b
        self.andGate1 = i.a & i.b

        self.andGate2 = self.carry & self.xorGate
        self.nandGate = ~self.andGate2
        self.orGate = self.carry | self.xorGate
        self.ansAndGate = self.orGate & self.nandGate

        self.norGate = ~(self.andGate1 | self.andGate2)
        self.carry = ~self.norGate
      


