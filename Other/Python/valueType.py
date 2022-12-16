#Keontae Trotman
#This program validates user input as even or odd and positive or negative.
#Traps the user in a loop to make sure their input is valid.
while True:
    try:
        #Asks user to input a number.
        x=int(input('Input an integer.\nX:'))
#Output
        #If the value is not an integer 
    except ValueError:
        print('Sorry, I did not understand that.')
    else:
        #Value was successfully parsed. Now the program can continue.
        #End loop.
        break
#Checks to see if the user input is even and positive.
if x>0 and x%2 == 0:
    print('x is positive and even.')
#Checks to see if user input is even and negative.
elif x<0 and x%2 == 0:
    print ('x is not positve and even.')
#Checks to see if user input is odd and positive.
elif x>0 and x%2 != 0:
    print ('x is positve and odd.')
#Checks to see if user input is odd and negative.
elif x<0 and x%2 != 0:
    print('x is not positive and odd.')
#Checks to see if user input is zero.
elif x==0:
    print('x is even and neither positive nor negative.')
