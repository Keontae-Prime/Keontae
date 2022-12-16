#Keontae Trotman
#This program generates positive random integers in the range of 1 to 500, counts each iteration, and outputs the highest number generated so far.
#Python package that generates random numbers. 
import random
#variable x starts at zero.
x=0
#Counter starts a zero.
count=0
#Represents the maximum value of x.
max=0
#While x isn't 500 keep looping.
while x != 500:
    #Count goes up by 1 per loop.
    count+=1
    #X is set as a random number every loop.
    x=random.randint(1,500)
    #Only prints x if the value is greater than the previous one.
    if max<x:
        #The variable max becomes the largest x
        max=x
        #The variable max or the largest x is printed
        print("The largest integer so far is: ", max)
    #The loop breaks when x finally becomes 500.
    if max==500:
        break
#The number of iterations it took to get to 500 is printed at the end.
print("It took ", count, "iterations to generate the number 500.")
