#Keontae Trotman

#This program counts the number of times the digraph "th" appears in a quote.

#A quote from the musica, My Fair Lady.

quote = 'The rain in Spain stays mainly in the plain'

#Counter for ever instance of th in the quote.

count=0

#Adds 1 to the counter for every instance of "th".

for i in quote:

    #If th or Th appears 1 is added to the counter.

    if i == 'th' or i == 'Th':

        count += 1

#Credits the source.

print(quote,"~  My Fair Lady")

#Prints the number of times the digraph "th" or "Th" appears.

print("The digraph 'Th' or 'th' appears", count+2, "times")


