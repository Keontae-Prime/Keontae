#Keontae Trotman
#This program simulates a game of rock paper scissors.
#Have the program run the loop, then ask if the user wants to continue. if yes restart loop
#if no end loop/program
#Initialize rock paper scissors stop at the beginning.
#Create get functions
#Create set functions
#Initialize user and cpu choice
import random
class rps:
    def __init__(self):
        self.__userScore=0
        self.__cpuScore=0

    def intro():
        print("Intro?(y/n)")
        selection=input()
        selection=selection.lower()
        if selection=='y':
            print("Please enter your name.")
            name=input()
            print("Hello",name+",","lets play some rock paper scissors!")
            return True
        if selection=='n':
            return True
            
    #intro()
    def main():
        userScore=0
        cpuScore=0
        print ('You:',userScore,'\t me:',cpuScore)
        choices=["rock","paper","scissors","Stop"]
        cpuTurn=random.choice(choices)
        print("Choose rock, paper, or scissors.")
        userTurn=input()
        userTurn=userTurn.lower()
        x=True
        print(userScore,cpuScore)
        x=True
        while x is True:
            if userTurn in choices:
                print("You selected",userTurn)
                print("I selected", cpuTurn)
            else:
                print("You must enter rock paper or scissors.")
            if userTurn==cpuTurn:
                print("We both selected",userTurn ,"It's a draw.")
            if userTurn=='rock' and cpuTurn=='scissors':
                print("Rock beats scissors. You win!")
                userScore+=1
                
            if userTurn=='scissors' and cpuTurn=='rock':
                print("Rock beats scissors. I win!")
                cpuScore+=1
                
            if userTurn == 'paper' and cpuTurn=='rock':
                print("paper beats rock. You win!")
                userScore+=1
            if cpuTurn == 'paper' and userTurn=='rock':
                print("paper beats rock. I win!")
                cpuScore+=1
            if userTurn=='paper' and cpuTurn=='scissors':
                print("Scissors beats paper. I win!")
                cpuScore+=1
            if cpuTurn=='paper' and userTurn=='scissors':
                print("Scissors beats paper. You win!")
                userScore+=1
            if userTurn=='stop':
                print('Goodbye')
                SystemExit
            x=False
            print('Contine? (y/n)')
            cRoad=input()
            if cRoad=='y':
                x=True
            else:
                SystemExit

    intro()