import time
#Keontae Trotman
#This program calls a function that prints the first stanza of Rober Frost's "The Road Not Taken"
#Part 1
#Function named poem ready to be called and will print the stanza when called.
def poem():
    print("Part 1:\nTwo roads diverged in a yellow wood,\nAnd sorry I could not travel both\nAnd be one traveler, long I stood\nAnd looked down one as far as I could\nTo where it bent in the undergrowth;")
#Part 2
#Time it takes for function to be called named "start".
start=time.perf_counter()
#The function "poem" is called
poem()
#Time it takes for function to end named "end".
end=time.perf_counter()
#Prints the start time, end time, and difference between start and end.
print("Part 2:\nStart:",start,"\nEnd:",end,"\nTime Elapsed:",end-start)
#Part 3
#New function named "clockWork".
def clockWork():
    #Calculates the start time
    start2=time.perf_counter()
    #Calculates the end time
    end2=time.perf_counter()
    #Prints the start and end time.
    print("\nPart 3:\nStart:",start2,"\nEnd:",end2,)
#Calls the function "clockWork"
clockWork()
#Part 4
#Start time
finalStart=time.perf_counter()
#End Time
finalEnd=time.perf_counter()
#New function name valReturn
def valReturn(x,y):
    #Returns the difference between two values
    return y-x
#Prints the difference between the start and end time.
print("\nPart 4:\n",valReturn(finalStart,finalEnd))
