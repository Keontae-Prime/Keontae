#Keontae Trotman.
#This program calculates the price of a gift box, which holds 6 chocolates and adds the sales tax.
#The cost of each chocolate.
darkHazel=1.40
darkRaspberry=1.10
milkOrange=1
milkCaramel=1.05
whiteCoffee=1.25
whitePecan=1.30
#My choice of chocolates
print("I want 2 dark hazel, 3 dark raspberries, and 1 white pecan.")
#Calculating the sum of my box without sales tax.
sum=(darkHazel*2)+(darkRaspberry*3)+(whitePecan)
#Calculating the sales tax.
salesTax=sum*(8.25/100)
#Adding the sales tax to the sum.
total=float(sum+salesTax)
#Outputting total including sales tax.
#Rounding to the 2nd decimal place.
print("The total for this box will be $",round(total,2),". Thank you for shopping with us!")



