#Keontae Trotman
#This program outputs a proverb upon request.
#Greeting
print("Hello This program will take your input of 1-7 and return /n a proverb according to the number you entered.")
print("Please enter a positive integer")
#Traps the user in a loop to make sure their input is valid.
while True:
    try:
        #Asks user to input a number.
        x=int(input())
#Output
        #If the value is not an integer 
    except ValueError:
        print('Sorry, I did not understand that.')
    else:
        #Value was successfully parsed. Now the program can continue.
        #End loop.
        break
#Returns the users input.
print("You entered", x)
#Converts the integer to a number between 0 and 6. 
n=x%7
#Returns the first proverb if the converted integer is 0
if n==0:
    print("A bad workman always blames his tools. \nThis describes workers who can't take responsibility for their lack of effort.")
#Returns the second proverb if the converted integer is 1
elif n==1:
    print("A cat has nine lives. \nThis means cats can survive seemingly fatal events.")
#Returns the third proverb if the converted integer is 2
elif n==2:
    print("A chain is only as strong as its weakest link. \nThis means One weak person on a team makes the rest of the team weak.")
#Returns the fouth proverb if the converted integer is 3
elif n==3:
    print("A drowning man will clutch at a straw. \nThis means that when our backs our against the wall, we will fight by any means necessary.")
#Returns the fifth proverb if the converted integer is 4
elif n==4:
    print("Adversity and loss make a man wise. \nThis means you can learn from failure.")
#Returns the sixth proverb if the converted integer is 5
elif n==5:
    print("A fool and his money are soon parted. \nThis means financially illiterate people can never be rich")
#Returns the seventh proverb if the converted integer is 6
elif n==6:
    print("All that glitters is not gold. \nThis means an outcome may look perfect, but the journey it took to get there was far from it.")
        
