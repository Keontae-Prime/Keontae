# Keontae Trotman
# This program reads through U.S mask data in each state and returns the average frequency that survey takers say they wear a mask along with the best and worst county in each state based on highest most frequently worn masks and highest least frequently worn masks.
# Imports csv library for processing csv files
import csv
def main():
    # Opens the area abbreviations file
    stateAbbreviations=open('State_abbreviations.csv')
    # Reads the area abbreviations file
    stateReader=csv.reader(stateAbbreviations)
    # opens geocodes file
    geocodes=open('State-geocodes-v2018.csv')
    # Reads geocodes file
    geocodesReader=csv.reader(geocodes)
    # Opens mask use file
    maskUse=open('mask-use-by-county.csv')
    # Reads mask use file
    maskReader=csv.reader(maskUse)
    # Skips headers
    next(stateReader, None)
    next(geocodes, None)
    next(maskReader, None)
    # Creates a dictionary for the all the data on each state (or at least everything important)
    fullData={}
    #List for geo data containing state name and FIPS
    geoData=[]
    # Creates a dictionary for the never category
    never={}
    # Creates a dictionary for the rarely category
    rarely={}
    # Creates a dictionary for the sometimes category
    sometimes={}
    # Creates a dictionary for the frequently category
    frequently={}
    # Creates a dictionary for the always category
    always={}
    # Creates a dictionary for the average never
    avgNever={}
    # Creates a dictionary for the average rarely
    avgRarely={}
    # Creates a dictionary for the average sometimes
    avgSometimes={}
    # Creates a dictionary for the average frequently
    avgFrequently={}
    # Creates a dictionary for the average always
    avgAlways={}
    # Reads through State-Geocodes csv
    for geo in geocodesReader:
        # Variable for state code
        stateFip=geo[1]
        # Variable for state name
        area=geo[6]
        # Code and name go to the geoData dictionary together
        if area not in geoData:
            geoData.extend([stateFip,area])
    #Reads through state abbreviation csv
    for state in stateReader:
        # Variable for full name of state
        name=state[0]
        # Variable for state abbreviation
        abbv=state[1]
        # Index variable finds the location of state name in geo csv
        index=geoData.index(name)
        # Abbreviation is added to the dictiionary at the location where the full state names match
        geoData.insert(index,abbv)
    #Reads through mask data csv
    for county in maskReader:
        # Variable for county fips
        countyFip=county[0]
        # Variable to calc worst mask data by adding never and rarely category
        worst=float(county[1])+float(county[2])
        # Varibale to calc best mask data by adding always and frequently
        best=float(county[4])+float(county[5])
        # Variable for finding index where the first 2 numbers of FIPS match
        index=geoData.index(countyFip[:2])
        # Varible for finding index with state abbreviation
        area=geoData[index+1]
        # Variable for finding index with state name
        state=geoData[index+2]
        # Adds never statistic for each county to never dictionary with the abbreviation as the key
        if area in never:
            never[area]+=[float(county[1])]
        # Adds never statistic for each county to never dictionary with the abbreviation as the key
        if area not in never:
            never[area]=[float(county[1])]
        # Adds rarely statistic for each county to rarely dictionary with the abbreviation as the key
        if area in rarely:
            rarely[area]+=[float(county[2])]
        # Adds rarely statistic for each county to rarely dictionary with the abbreviation as the key
        if area not in rarely:
            rarely[area]=[float(county[2])]
        # Adds sometimes statistic for each county to sometimes dictionary with the abbreviation as the key
        if area in sometimes:
            sometimes[area]+=[float(county[3])]
        # Adds sometimes statistic for each county to sometimes dictionary with the abbreviation as the key
        if area not in sometimes:
            sometimes[area]=[float(county[3])]
        # Adds frequently statistic for each county to frequently dictionary with the abbreviation as the key
        if area in frequently:
            frequently[area]+=[float(county[4])]
        # Adds frequently statistic for each county to frequently dictionary with the abbreviation as the key
        if area not in frequently:
            frequently[area]=[float(county[4])]
        # Adds always statistic for each county to always dictionary with the abbreviation as the key
        if area in always:
            always[area]+=[float(county[5])]
        # Adds always statistic for each county to always dictionary with the abbreviation as the key
        if area not in always:
            always[area]=[float(county[5])]
        # Reads through never dictionary and calculates the average for each state based on FIP
        for k,v in never.items():
            avgNever[k]=round((sum(v)/ float(len(v))),3)
        # Reads through rarely dictionary and calculates the average for each state based on FIP
        for k,v in rarely.items():
            avgRarely[k]=round((sum(v)/ float(len(v))),3)
        # Reads through sometimes dictionary and calculates the average for each state based on FIP
        for k,v in sometimes.items():
            avgSometimes[k]=round((sum(v)/ float(len(v))),3)
        # Reads through frequently dictionary and calculates the average for each state based on FIP
        for k,v in frequently.items():
            avgFrequently[k]=round((sum(v)/ float(len(v))),3)
        # Reads through always dictionary and calculates the average for each state based on FIP
        for k,v in always.items():
            avgAlways[k]=round((sum(v)/ float(len(v))),3)
        # Adds all the important data collected to the fullData dictionary
        if area not in fullData:
            fullData[area]=round(best,3),countyFip,round(worst,3),countyFip,avgNever[area],avgRarely[area],avgSometimes[area],avgFrequently[area],avgAlways[area],state
        # Replaces the lowest best with the highest best for each county
        if area in fullData and fullData[area][0]<best:
            fullData[area]=round(best,3),countyFip,round(fullData[area][2],3),fullData[area][3],avgNever[area],avgRarely[area],avgSometimes[area],avgFrequently[area],avgAlways[area],state
        # Replaces the lowest worst with the highest worst for each county
        if area in fullData and fullData[area][2]<worst:
            fullData[area]=round(fullData[area][0],3),fullData[area][1],round(worst,3),countyFip,avgNever[area],avgRarely[area],avgSometimes[area],avgFrequently[area],avgAlways[area],state
    #Intro
    print('\nThis program outputs the mask wearing categories for all or a given state in the U.S')
    # active variable for controlling while loop
    active=True
    # Program begins
    while active:
        #Informs the user what to input.
        print('Acceptable inputs:\nAll\nState Abbreviation\nExit\n')
        #Allows the user to make an input.
        userInput=input('Please enter a valid command.\n')
        #Converts user input to uppercase letters.
        x=userInput.upper()
        # If user inputs all give all states with categories with best and worst counties
        if x==('ALL'):
            # Reads through dictionary and formats output so that it's readable
            for item, amount in fullData.items():  
                print("\nState Name:",amount[9],"\nAlways:",'{0:.0%}'.format(amount[8]),"\nFrequently:",'{0:.0%}'.format(amount[7]),"\nSometimes:",'{0:.0%}'.format(amount[6]),"\nRarely:",'{0:.0%}'.format(amount[4]),"\nNever:",'{0:.0%}'.format(amount[5]),
                "\nWorst County:",amount[3],"with",'{0:.0%}'.format(amount[2]),"Never or rarely wearing masks","\nBest County:",amount[1],"with",'{0:.0%}'.format(amount[0]),"Frequently or always wearing a mask\n")
        #If user inputs exit, close the program.
        elif x==('EXIT'):
            print('Goodbye.')
            active=False
        # if user inputs a state abbreviation print out every category with percentages and best and worst county
        elif x in fullData.keys():
            print("\nState Name:",fullData[x][9],"\nAlways:",'{0:.0%}'.format(fullData[x][8]),"\nFrequently:",'{0:.0%}'.format(fullData[x][7]),"\nSometimes:",'{0:.0%}'.format(fullData[x][6]),"\nRarely:",'{0:.0%}'.format(fullData[x][4]),"\nNever:",'{0:.0%}'.format(fullData[x][5]))
            print("Worst County:",fullData[x][3],"with",'{0:.0%}'.format(fullData[x][2]),"Never or rarely wearing masks","\nBest County:",fullData[x][1],"with",'{0:.0%}'.format(fullData[x][0]),"Frequently or always wearing a mask\n")
        # Prints this if no valid command is entered
        else:print("\nState not found. Please try again.\n")
#Runs the program
main()