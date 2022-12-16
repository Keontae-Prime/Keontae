#Keontae Trotman
#This program Find the sum of the first 100 terms of the series of 1/10 1/100 1/1000...
#The counter starts at 1
count = 1
#Running total represents each number in the series starting at 1
runningTotal=1
#x is the variable used to add each number in the series and starts at 0.
x=0
#Loop that runs as long as the counter is less than 100.
while(count <= 100):
    #Counter goes up by 1 per cycle.
    count += 1
    #Running total gets multiplied by itself each cycle
    runningTotal*=0.1
    #x becomes the running total then adds itself each cycle
    x+=runningTotal
#Output
#The sum of the first 100 terms in the series is printed.
print("Sum =", x)
