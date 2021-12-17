#Keontae Trotman
#This program checks and calculates ISBN.
import sys
isbn=input("Please enter a 10 digit number for the ISBN check digit:  ")
while len(isbn)!= 10:
    try:
        isbn=int(input("Please enter the 10 digit number again: "))
    except ValueError:
        print("Please try again and make sure you entered 10 digits.")
    break
else:
    D1 =int(isbn[0])*11
    D2 =int(isbn[1])*10
    D3 =int(isbn[2])*9
    D4 =int(isbn[3])*8
    D5 =int(isbn[4])*7
    D6 =int(isbn[5])*6
    D7 =int(isbn[6])*5
    D8 =int(isbn[7])*4
    D9 =int(isbn[8])*3
    D10=int(isbn[9])*2
    Sum=(D1+D2+D3+D4+D5+D6+D7+D8+D9+D10)
    Mod=Sum%11
    D11=11-Mod
    if D11==10:
        D11='X'
    ISBNNumber=str(isbn)+str(D11)
    print("Your 11 digit ISBN Number is *" + ISBNNumber + "*")
sys.exit(0)
