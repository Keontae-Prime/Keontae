#Keontae Trotman
#This program takes two non-zero numbers and divides them.
#Function that checks whether or not the numbers are zero.
#Imports that help stop the program if user doesn't input a number.
import sys
def num1():
    #If it's not zero, continue to next function
    if y != 0:
       num2()
    #If it's zero give user a message.
    elif y==0:
        print("You cannot divide by zero.")
#Function that divides the first number by the second number.
def num2():
    z=x/y
    print("The quotient is:",z)

#Makes sure their input is valid.
try:
    #Asks user to input a number.
    x=float(input('Enter a number:\n'))
    y=float(input('Enter another number:\n'))
#Output
#If the value is not a float give the user an error message and close the program.
except ValueError:
    print("Sorry, but you have to enter a number\nThe program will now stop.")
    sys.exit(0)
#output
num1()
