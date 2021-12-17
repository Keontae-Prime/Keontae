#Keontae Trotman
#This program checks to make sure a password meets a certain criteria.
#Greeting
print('Hello. This program will validate a correctly written password.')
print('''The rules:\nMust contain 4 digits.\nMust contain 3 letters.
Must begin with a letter.\nMust contain a ^ that is also the 2nd element of your password.''')
#Funtion.
def validator():
#Traps user in a loop and the only way to escape is through entering a valid
#password.
    while True:
        password=input()
        #Password must begin with a letter.
        if (password[0].isalpha())!=True:
            #Error if the first character isn't a letter.
            print('Must begin with a letter.')
        #2nd element of the password must have a "^"
        for i in password[1]:
            if i != '^':
                #Error message if the 2nd element isn't a ^.
                print('Must contain ^ as second element')
        #Must have at least 4 digits
        if len([i for i in password if i.isdigit()]) < 4:
            #Error message if at least 4 digits are not present.
            print('Must contain 4 digits.')
        #Must have at least 3 letters.
        elif len([i for i in password if i.isalpha()]) < 3:
            #Error message if at least 3 letters are not present.
            print('Must contain 3 letters.')
        #Password must be at least 7 characters.
        elif len(password)<7:
            #Error if password is less than 7 characters.
            print("Too Short")
        #If all these reqirements are met the loop breaks.
        else:
            break
#Output
#Calls the function
validator()
#Lets the user know they entered their password correctly.
print('This password is valid.') 
