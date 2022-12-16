#Keontae Trotman
#This program counts the number of times N,R,T appears in a quote.
#A famous quote by Nelson Mandela.
quote='''The greatest glory in living lies not in never falling, but in
rising every time we fall.'''
#Counter for every instance of N in the quote.
countN=0
#Counter for every instance of R in the quote.
countR=0
#Counter for every instance of T in the quote.
countT=0
#Variable x copies the quote, but in lower case.
x=quote.lower()
#Adds 1 to each counter for every instance of its respective character.
for i in x:
    if i=='n':
        countN += 1
    elif i=='r':
        countR += 1
    elif i=='t':
        countT += 1
#Credits the speaker
print(quote,"~ Nelson Mandela")
#Prints the number of times the letter n appears.
print("n appears", countN, "times")
#Prints the number of times the letter r appears.
print("r appears", countR, "times")
#Prints the number of times the letter t appears.
print("t appears", countT, "times")

