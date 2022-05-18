#Keontae Trotman
#This program reads and prints unique vehicles from a csv file.
#Traps the user in a loop that can only be broken once the input file can be found.
import csv
while True:
        try:
            #Must download the following file
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
def main():
    #One of the words being looked for.
    fuel=("Gasoline")
    #Another word being looked for.
    cars=("Cars")
    #placeholder for all the makes with cars and gasoline in them
    duplicates=[]
    #Placeholder for sorted unique makes.
    uniqueMakes=[]
    #Fuel type: 31, Make: 46, Type: 62, City: 4, Hiway:34
    print('List of unique vehicles:')
    #Placeholder for minimum cityMPG
    minim=[]
    #Placeholder for lowest hiwayMPG
    minim2=[]
    #Large numbers to be replaced by lowest MPG.
    min=1000000
    min2=1000000
    #Reads ever row in the reader.
    for row in reader:
        #Represents cityMPG
        city=[row[46],row[47],float(row[4]),row[31],row[62]]
        #If it has 'gasoline' and 'cars' in it and has a MPG lower than the previous continue.
        if city[2]<min and fuel in city[3] and cars in city[4]:
            #1 million and previous mins gets replaced by new minimum
            min=city[2]
            #List gets cleared
            minim.clear()
            #To make room for the new list.
            minim.append(city[0:3])
        #Represents HiwayMPG
        hiWay=[row[46],row[47],float(row[34]),row[31],row[62]]
        #If it has 'Gasoline' and 'Cars' in it and has a lower MPG than the previous continue.
        if hiWay[2]<min2 and fuel in hiWay[3] and cars in hiWay[4]:
            #Previous mins gets replaced by new min.
            min2=hiWay[2]
            #List gets cleared
            minim2.clear()
            #To make room for new list.
            minim2.append(hiWay[0:3])
        #Combines the 3 lists into one comma separated list
        x=[row[31],row[46],row[62]]
        #if words are found in a list append it. If not, do nothing.
        if fuel in x[0] and cars in x[2]:
            duplicates.append(x[1])
    #Reads every row in duplicates
    for makes in duplicates:
        #Creates a uniqe list.
        if makes not in uniqueMakes:
            uniqueMakes.append(makes)
            #Sorts unique list alphabetically.
            uniqueMakes.sort()
    for i in uniqueMakes:
        #Outputs sorted unique makes
        print(i)
    #Removes brakets from MPG lists    
    res=str(minim)[2:-2]
    res2=str(minim2)[2:-2]
    #Outputs Lowes city and hiway MPGs.
    print('\nLowest City MPG:\n')
    print (res,'\n')
    print('Lowest hiway MPG:\n')
    print (res2,'\n')
main()
