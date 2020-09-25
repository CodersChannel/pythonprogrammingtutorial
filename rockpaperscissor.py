import random # 'random' is module having different functions, here we are using it to genearte random numbers within a specified range
import sys # 'sys' provides functions and variables used to manipulate different parts of the Python runtime environment.

'''
Below are ansi codes for setting the color, It is just for practice if you want to use colored text in large application then use
any library like 'termcolor','Colorama' etc.
'''
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
BOLDTEXT = '\033[1m'
ENDCOLOR = '\033[0m'

def printblue(text):
    print(BLUE,BOLDTEXT,text,ENDCOLOR)

def printred(text):
    print(RED,BOLDTEXT,text,ENDCOLOR)

def printgreen(text):
    print(GREEN,BOLDTEXT,text,ENDCOLOR)


# below function is used chooose number in range from 0 to 2 and map that number to 'r' if 0, 'p' if 1 and 's' if 2
def computerchoice():
    num = random.randint(1,3)
    if num==1:
        return 'r'
    elif num==2:
        return 'p'
    elif num==3:
        return 's'

# below function map 'r'->'rock', 'p'->'paper' and 's'->'scissor'
def rpstofullname(input):
    if input=='r':
        return 'rock'
    elif input=='p':
        return 'paper'
    elif input=='s':
        return 'scissor'


username = input("Please enter you name: ")
print("Hi %s, lets begin the game."%(username))

while True:
    # in below line '\n' is used to print text after it ('\n') in new line
    userchoice = input("Please enter your choice:\n 'r' for rock \n 'p' for paper \n 's' for scissor \n 'q' for quit \n")
    if userchoice=='q':
        sys.exit("closing the game, good bye!!") # sys.exit() is used to exit the program, it is optional to pass text as argument inside it.
        # the passed text will print before the closing of the program.

    print('user select : %s'%(rpstofullname(userchoice)))
    compchoice = computerchoice()
    print('computer select : %s'%(rpstofullname(compchoice)))

    print('%s vs %s'%(rpstofullname(userchoice),rpstofullname(compchoice)))

    if userchoice == compchoice:
        printblue("It's a tie!")
    elif userchoice == 'r' and compchoice == 's':
        printgreen('You win!')
    elif userchoice == 'p' and compchoice == 'r':
        printgreen('You win!')
    elif userchoice == 's' and compchoice == 'p':
        printgreen('You win!')
    elif userchoice == 'r' and compchoice == 'p':
        printred('You lose!')
    elif userchoice == 'p' and compchoice == 's':
        printred('You lose!')
    elif userchoice == 's' and compchoice == 'r':
        printred('You lose!')
    print('---------------------------------------')
