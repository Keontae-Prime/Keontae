#Keontae Trotman
#This program asks the user to choose a famous person, enter the first and last name of that person, the person's birth day, birth month and birth year and returns that person's current age.
#Greets and asks the user to input the first and last name of a famous person.
print("Hello, please think of and enter the first and last name of a famous person")
while True:
    try:
        #Asks user to input a string.
        x=str(input())
    except ValueError:
        print("Please enter their full name.")
    else:
        #Value was successfully parsed. Now the program can continue.
        #End loop.
        break
#Asks user to enter the celebrities birth year.
print("please enter the birth year of", x)
while True:
    try:
        #Asks user to input an int.
        year=int(input())
    except ValueError:
        print("Sorry please try again")
    else:
        #Value was successfully parsed. Now the program can continue.
        #End loop.
        break
#Asks user to enter the celebrities birth month.
print("please enter the birth month of", x,"as a number.")
while True:
        try:
            #Asks user to input an int.
            month=int(input())
        except ValueError:
            print("Sorry please try again")
        else:
        #Value was successfully parsed. Now the program can continue.
        #End loop.
            break
#Converts the input number into a day of the corresponding day of the month.
if month==1:
    month=str('January')
elif month==2:
    month=str('February')
elif month==3:
    month=str('March')
elif month==4:
    month=str('April')
elif month==5:
    month=str('May')
elif month==6:
    month=str('June')
elif month==7:
    month=str('July')
elif month==8:
    month=str('August')
elif month==9:
    month=str('September')
elif month==10:
    month=str('October')
elif month==11:
    month=str('November')
elif month==12:
    month=str('December')
#Asks user to enter the celebrities birth day.
print("please enter the birth day of", x)
while True:
    try:
        #Asks user to input a string.
        day=int(input())
    except ValueError:
            print("Sorry please try again")
    else:
        #Value was successfully parsed. Now the program can continue.
        #End loop.
        break
#Prints the celebrities full name, birth month, birth day, and birth year
print("Name:", x,"\nBirth month:", month,"\nBirth day:",day,"\nBirth year:",year)
#Current year
cYear=2020
#Calculates the celebrites age:
age=cYear-year
#Prints the celebrities age:
print("Age:", age,"years old")

