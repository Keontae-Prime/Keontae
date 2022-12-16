#Keontae Trotman
#This program requests a phone number and returns it correctly.
#Greeting
print('Hello. This program will take your phone number and format it properly')
#User enters their number
phone=str(input('please input your ten digit phone number. \n'))
#Blank variable to copy reworked output.
result=''
#Seeks out instances of (,),and - and replaces it with a blank, thus removing it.
for i in phone:
    if i==('-') or i==('(') or i==(')'):
        i=''
    #Reworked number format is copied to result.
    result+=i
#Result is printed if 10 digits.
if len(result)==10:
    print('Proper format:',result)
#Error sent if less than or equal to 10 digits.
else:
    print("Sorry,this is not a valid phone number.")


