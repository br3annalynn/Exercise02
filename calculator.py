'''
checks:
number of tokens YES
numbers vs letters YES
0's mod, division YES
decimals
'''

import arithmetic
from sys import exit

def main():

    while True:
        
        #get operation and numbers from user
        user_input = raw_input("> ")
        #split operations and numbers
        tokens = user_input.split(" ")

        check = check_args(tokens) #This checks the number of arguments the user enters

        if check == "y":
            #find correct operation
            if tokens[0] == "+":
                print arithmetic.add(int(tokens[1]), int(tokens[2])) # check: can we do tokens[1, 2]?
                # make sure there are 2 arguments
            elif tokens[0] == "-":
                print arithmetic.subtract(int(tokens[1]), int(tokens[2])) # 2 args
            elif tokens[0] == "*":
                print arithmetic.multiply(int(tokens[1]), int(tokens[2])) # 2 args
            elif tokens[0] == "/":
                print arithmetic.divide(float(tokens[1]), int(tokens[2])) # zero
            elif tokens[0] == "square":
                print arithmetic.square(int(tokens[1])) # 1 arg
            elif tokens[0] == "cube":
                print arithmetic.cube(int(tokens[1])) # 1 arg
            elif tokens[0] == "pow":
                print arithmetic.power(int(tokens[1]), int(tokens[2])) # 2 args
            elif tokens[0] == "mod":
                print arithmetic.mod(int(tokens[1]), int(tokens[2])) # zero
            #elif tokens[0] == "q":
                #exit(0)
            #else:
                #print "That entry didn't compute. Try again."
            # make sure all are numbers

def check_args(tokens):
    if tokens[0] == "q" and len(tokens) == 1:
        exit(0)

    elif tokens[0] == "+" or tokens[0] == "-" or tokens[0] == "*" or tokens[0] == "/" or tokens[0] == "pow" or tokens[0] == "mod":
        if len(tokens) != 3:
            check = "n"
            print "Wrong number of entries. Try again." 
        elif tokens[1] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] or tokens[2] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            check = "n" 
            print "That's not an integer number. Try again." 
        elif tokens[0] == "/" or tokens[0] == "mod":
            if tokens[2] == "0":
                check = "n"
                print "Cannot divide by zero"
            else:
                check = "y" 
        else: 
            check = "y"


    elif tokens[0] == "square" or tokens[0] == "cube":
        if len(tokens) != 2:
            check = "n"
            print "Wrong number of entries. Try again." 
        elif tokens[1] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            check = "n" 
            print "That's not an integer number. Try again."  
        else:
            check = "y"
    
    elif tokens[0] not in ["+", "-", "*", "/", "pow", "cube", "square", "mod", "q"]:
        check = "n"
        print "Not a correct function. Try again."


    return check



main()


