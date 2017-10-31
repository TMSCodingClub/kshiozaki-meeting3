#Date: 10/03/2017
#concept: blackjack
import random

score = 0

def decide(input):
    if (input == "hit"):
        return True
    elif (input == "stop"):
        return False

def randomCard():
    card = random.randint(1,13)
    if(card>10):
        return 10
    else:
        return card

while(True):
    print("Your score is ",score)
    words = input()
    if(decide(words)):
        print("you get a card")
        score = score + randomCard()
    else:
        print("No")
    
    if(score>21):
        print("GAME OVER")
        
#terminal commands:
    #terminate program: ctrl + z
    #set destination: "cd desktop"
    #open a file: python3 __(file name)__.py
