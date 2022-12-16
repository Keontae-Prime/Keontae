#Keontae Trotman
#This program enycrypts a file using public private key contained in file.
import sys
def open_files():
    #Traps the user in a loop that can only be broken once an input file path is found.
    while True:
        try:
            #prompts user to input file path
            myFile=input('Enter the path to the file:\n')
            #Opens the file
            f = open(myFile,'r')
            #Stores the first line as a variable
            x=f.readline()
            #Stores the rest of the lines as a variable and removes trailing whitespace.
            t=f.read()
        #Prints error and restarts loop if file path not found.
        except FileNotFoundError:
            print('This file could not be found. Please try again.')
        #Prompts user that path was found and closes the file.
        else:
            print('Found the file!\n')
            f.close()
            #Saves the variables
            return x,t
def main():
    #Variables from previous function get passed on
    x,t=open_files()
    #lowercase alphabet for transversal reference
    alpha='abcdefghijklmnopqrstuvwxyz'
    #uppercase alphabet for transversal reference
    beta='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #numbers for transversal reference
    charlie='1234567890'
    #Converts into tuples
    myTuple=tuple(alpha)
    myTuple2=tuple(beta)
    myTuple3=tuple(charlie)
    #Empty list to get appended words in file
    enycryptedWord=[]
    #Makes sure file begins with number
    if x.startswith(tuple('0123456789')):
        #key becomes the number
        key=int(x[0])
    else: 
        #Error message and closes program
        print('Error: No key found.')
        sys.exit(0)
    #Loop for shifting words and numbers in file
    for word in t:
        #if its a lowercase letter shift
        if word.strip and word in myTuple:
            enycryptedWord.append(myTuple[(myTuple.index(word) + key) % 26])
        #if uppercase letter shift
        elif word.strip and word in myTuple2:
            enycryptedWord.append(myTuple2[(myTuple2.index(word) + key) % 26])
        #if number shift
        elif word.strip and word in myTuple3:
            enycryptedWord.append(myTuple3[(myTuple3.index(word) + key) % 10])
        #if neither ignore
        else: 
            enycryptedWord.append(word)
    #Turns list into strings/ reformats back to original file style
    output=''.join(enycryptedWord)
    #Prints the output
    print('Enycrpted Output:\n',output)
    #Creates a new file
    outfile = open('Secure.txt', 'w')
    #Writes the output to the file
    outfile.write(output)
    #Closes the file.
    outfile.close()
#Calls the main function
main()
