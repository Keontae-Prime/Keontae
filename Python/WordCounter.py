#Keontae Trotman
#This program opens a txt file and counts each line and occurence of "and" and "or"
#Greeting
print('''Hello this program will count each use of the words "and" and
"or" in a txt file.''')
#Counter for each line in the file. Set at 0.
lineCount=0
#Counter for each instance of 'and' in the file. Set at 0.
andCount=0
#Counter for each instance of 'or' in the file. Set at 0.
orCount=0
#Variable representing the string 'and'
word1='and'
#Variable representing the string 'or'
word2='or'
#Traps the user in a loop that can only be broken once the input file can be found.
while True:
    try:
        myFile=input('Enter the name of a txt file:\n')
        f = open(myFile,'r')
    except FileNotFoundError:
        print('This file could not be found. Please try again.')
    else:
        print('Found it!')
        break
#Loop that reads through each word in the file.
for line in f:
    #For every instance of \n, which represents a new line, 1 gets added to the line counter.
    lineCount=lineCount+1
    #For every instance of the word and, 1 gets added to the corresponding counter.
    if word1 in line.split():
        andCount += 1
    #For every instance of the word or, 1 gets added to the corresponding counter.
    if word2 in line.split():
        orCount += 1
#prints the number of times 'and' appears.
print ('The word',word1,'appears', andCount,'times.')
#prints the number of times 'or' appears.
print ('The word',word2,'appears', orCount,'times.')
#Prints the number of lines in the file.
print('There are', lineCount, 'lines in this file.')