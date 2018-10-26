import random
def generateRandomnum():
    randomnum=random.randint(1,3)
    return randomnum

def CompChoice(randnum):
    if(randnum == 1):
        computerchoice ="scissors"
    elif (randnum == 2):
        computerchoice ="paper"
    elif (randnum == 3):
        computerchoice ="rock"
    return computerchoice

def userchoice():
    userchoice=input("\nenter choice :")
    return userchoice

def Winner(userchoice , computerchoice):
    if (computerchoice == "rock" and userchoice == "scissors" ):
        print ("computer wins")
    elif (computerchoice == "scissors" and userchoice == "rock" ):
        print ("you win")
    elif (computerchoice == "scissors" and userchoice == "paper" ):
        print ("computer wins")
    elif (computerchoice == "paper" and userchoice == "scissors" ):
        print ("you win")
    elif (computerchoice == "paper" and userchoice == "rock" ):
        print ("computer wins")
    elif (computerchoice == "rock" and userchoice == "paper" ):
        print ("you win")
    elif ( computerchoice == userchoice ):
        print ("It's a tie!") 

if __name__=='__main__':
    ch="y"
    while ( ch == "y" or ch == "Y" ):
        randnum=generateRandomnum()
        ComputerChoice=CompChoice(randnum)
        UserChoice=userchoice()
        print ("Computer's choice is:",ComputerChoice )
        print ("Your choice is:",UserChoice )
        Winner (UserChoice, ComputerChoice )
        print ("Do you want to continue?(y/n)")
        ch=input()
    print ("Hope you join us next time!")




















