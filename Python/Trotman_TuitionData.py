# Keontae Trotman
# This program gives a predicted tuition rise for up to 2 years given previous state data
import csv
from Trotman_tuitionPrediction import prediction as pd
def main():
    #Years var holds list
    years=[]
    #Data variable holds dictionary
    data={}
    #tuitionData var opens csv
    tuitionData=open(r'us_avg_tuition.csv')
    #reader var uses csv lib to read csv
    tuitionReader=csv.reader(tuitionData)
    for row in tuitionReader:
        #Extends years to list while also removing some blank spaces.
        years.extend([s.replace('  ','') and s.replace(' ','') for s in row[0:]])
        #Removes unnecessary header
        years.pop(0)
        break
    years=([years[i:i+2] for i in range(0, len(years))])
    #Scans through rows in csv file
    for row in tuitionReader:
        #Gets list of tuition for each year
        tuitionList=list(row[1:])
        #Removes dollar sign from list
        tuitionList=[s.replace('$','') for s in tuitionList]
        #Removes comma from list
        tuitionList=[s.replace(',','') for s in tuitionList]
        #Converts string list into int list
        tuitionList=[int(s) for s in tuitionList]
        #Appends converted list in dictionary w/ state as key
        data[row[0].upper()]=tuitionList
    active=True
    # Program begins
    while active:
        #Informs the user what to input.
        print('Acceptable inputs:\nAll\nState Name\nExit\n')
        #Allows the user to make an input.
        userInput=input('Please enter a valid command.\n')
        #Converts user input to uppercase letters.
        userInput=userInput.upper()
        # If user inputs all give all states with predicted rise, annual rise, and average rise
        if userInput=='ALL':
            #Loops through an item in a dictionary
            for item,amount in data.items():
                #Prints the average and annual rise from prediciton class
                print(str(item)+':',"\nAverage Rise:",pd.getAverageRise(amount),"\nAnnual Rise:")
                #Links year w/ annual rise
                for x,y in zip(years,pd.getAnnualRise(data[item])):
                    #prints linked years and rises
                    print(str(x)+":",y)
                #Prints one year and two year prediction for state in each loop
                print("One year rise prediction:",pd.predAnnualRise(data[item]),"\nTwo Year rise Prediction:",pd.predBiennialRise(data[item]))
        # If user inputs a state see if its in data and give state with predicted rise,annual rise, and average rise
        elif userInput in data.keys():
            #Prints state from dict and average rise from prediction class
            print(userInput+":","\nAverage Rise:",pd.getAverageRise(data[userInput]),"\nAnnual Rise:")
            ##Links year w/ annual rise
            for x,y in zip(years,pd.getAnnualRise(data[userInput])):
                ##prints linked years and rises
                print (str(x)+":",y)
            print("One year rise prediction:",pd.predAnnualRise(data[userInput]),"\nTwo Year rise Prediction:",pd.predBiennialRise(data[userInput]))
        # If user inputs exit, exit the program
        elif userInput=='EXIT':
            active=False
main()
