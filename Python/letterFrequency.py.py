#Keontae Trotman
#This program uses a for loop to count the number of times the letter “e” appears in a string.
#Accumulator variable.
count=0
#String text from “The Rime of the Ancient Mariner” by Samuel Taylor Coleridge.
quote= "We were the first that ever burst Into that silent sea."
for i in quote:
    #Looks for every iteration of the letter e.
    if i == 'e':
        #Adds 1 to accumulator whenever e is found in the
        count=count + 1
#Output.
#Prints the number of times the letter e appears in text.
print('e appears', count, 'times')
