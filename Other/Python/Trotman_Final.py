#Keontae Trotman
#This program generates numbers from 1-100, adds up number not divisible by
#2 or 3 then prints the total and any duplicates.
# Function that creates a list from start to end
def num(start, end):
    #captures all numbers in range from x to y
    return [item for item in range(start, end+1)]
#Sets start to 0
start=0
#Sets end to 100
end=100
#Prints the numbers from 1-100 by adding to next num in list until 100 is met.
print(num(start, end))
#Total will be used to add up all numbers not divisible by 2 or 3.
total=0
#Checks every number in the list
for i in num(start,end):
    #Sees if each number is not divisible by 2 or 3.
    if (i % 2 != 0 and i % 3 != 0):  
        #adds to total if not
        total += i
#x becomes the string version of the total
x=str(total)
#prints the final total as a string
print("Total of numbers not divisible by 2 or 3:",x)
#splits total into list
y=[int(i) for i in x]
#Finds duplicates among the split list and prints them.
if y[0]==y[1]:
    print('Digits 1 and 2 are duplicates')
elif y[0]==y[2]:
    print('Digits 1 and 3 are duplicates')
elif y[0]==y[3]:
    print('Digits 1 and 4 are duplicates')
elif y[1]==y[2]:
    print('Digits 2 and 3 are duplicates')
elif y[1]==y[3]:
    print('Digits 2 and 4 are duplicates')
elif y[2]==y[3]:
    print('Digits 3 and 4 are duplicates')
        


