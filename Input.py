"""Module to take input from user, convert the input to binary and display in a list"""


class Input:
    def userInput(self):
        while True:
            self.a=int(input("Enter the first 8 bit number: "))
            self.b=int(input("Enter the second 8 bit number: "))
                
            if(self.a > 255 or self. b > 255) or (self.a < 0 or self.b < 0): #If condition the check if the input is valid or not
                print("\nInvalid input. Enter positive integer less than 256\n")
                continue
            
            else:                                                           #Codes to convert the input to binary and display it in a lisst if the input is valid
                self.firstNum = str(bin(self.a))[2:].zfill(8)
                self.firstNumList = list(self.firstNum)
                
                self.secondNum = str(bin(self.b))[2:].zfill(8)
                self.secondNumList = list(self.secondNum)

                self.c = 0
                while self.c < 8:                                                   #While loop to convert String to integer
                    self.firstNumList[self.c] = eval(self.firstNumList[self.c])
                    self.secondNumList[self.c] = eval(self.secondNumList[self.c])
                    self.c = self.c + 1

                print("\nConversion of the first 8 bit number: " ,self.firstNumList)
                print("\nConversion of the second 8 bit number: " ,self.secondNumList)
                break


