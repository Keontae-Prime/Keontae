#Keontae Trotman
#This program takes online reservatiions at the Red Tide Resort.
#Asks for clients for their name.
name=input('What is your name?\n')
#Greeting
print("Hello",name,"thank you for choosing Red Tide Resort.")
#Informing user of the room rate.
print("The room rental rate is $125 per night.")
#Inform user of habitation tax
print("Habitation Tax will be $5 per night.")
#Asks clients how many days they will be staying.
nights=int(input('How many nights will you be staying?\n'))
#Calculating room rental ($125 per night)
cost=125*nights
#Calculating sales tax.
salesTax=cost*(7.5/100)
#Calculating habitation tax.
habitation=5*nights
#Calculating total.
sum=cost+salesTax+habitation
#Output
#Print total nights.
print("Number of nights:",nights)
#print cost excluding tax.
print("Cost excluding tax:",cost,"usd")
#print sales tax in money format.
print("Sales Tax:",round(salesTax,2),"usd")
#Print habitation cost
print("Habitation cost:",habitation,"usd")
#Print total cost of rsvp in money format.
print("total cost",round(sum,2),"usd")







