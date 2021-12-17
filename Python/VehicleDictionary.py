#Keontae Trotman
#This program reads EPA Vehicle Data and creates a dictionary of makes with the lowest city MPG.
import csv
#Traps the user in a loop that can only be broken once the input file can be found.
def main():
    while True:
        try:
            #EPA Vehicle Data.csv
            myFile=input('Enter the path to the CSV file:\n')
            file=open(myFile)
            #Opens the file and reads it. Stores headers in dictionary.
            reader = csv.reader(file,delimiter=',')
            #Skips header
            next(reader, None)
            #Prints and loops if file cannot be found.
        except FileNotFoundError:
            print('This file could not be found. Please try again.')
            #breaks loop.
        else:
            print('Found it!')
            break
    #phonebook = {'Chris':'555−1111', 'Katie':'555−2222', 'Joanne':'555−3333'}
    #Empty Dictionary
    myDict={}
    #Loops through each row in csv file
    for row in reader:
        #Sets the make with corresponding row and converts it to uppercase.
        make=(row[46].upper())
        #Sets model with corresponding row.
        model=row[47]
        #Sets city with corresponding row and converts to int
        city=int(row[4])
        #Sets hiway with corresponding row and converts to float
        #When set to int I get "ValueError: invalid literal for int() with base 10: '0.0'""
        hiway=float(row[34])
        #If make not already in dictionary add it.
        if make not in myDict:
            myDict[make]=[model,city,hiway]
            city,model,hiway=myDict[make]
        #If make already in dictionary and has a greater cityMPG replace it.
        elif make in myDict and myDict[make][1]>city:
            myDict[make]=[model,city,hiway]
            city,model,hiway=myDict[make]
    #While Active is true, loop.
    active=True
    while active:
        #Informs the user what to input.
        print('Acceptable inputs:\nlist\nexit')
        #Allows the user to make an input.
        userInput=input('Please enter a valid command.\n')
        #Converts user input to lowercase letters.
        x=userInput.lower()
        #If user inputs exit, close the program.
        if x==('exit'):
            print('Goodbye.')
            active=False
        #If user inputs list, ask to input all or a make.
        elif x==('list'):
            #Allows the user to input.
            userInput2=input('Enter a vehicle make or "all"\n')
            #Converts the input to uppercase
            y=userInput2.upper()
            #If all, print the whole dictionary.
            if y==('ALL'):
                print('\nmake\t[Model,CityMPG,HiwayMPG]')
                for key, value in myDict.items():
                    print(key,value)
            #If user enters a specific make, print the model, cityMPG, and hiwayMPG.
            elif y in myDict:
                print('\nMake\tModel\tCityMPG\tHiwayMPG\n')
                print('\n',y,myDict[y],'\n')
            #Error and resets loop if input is invalid.
            else:
                print('Unacceptable Input. Please try again.\n')
        #Error and resets loop if input is invalid.
        else:
            print('Unacceptable Input. Please try again.\n')
#Calls the main function.
main()