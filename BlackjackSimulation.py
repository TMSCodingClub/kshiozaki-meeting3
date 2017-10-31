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

#10/31/2017
#To upload a file as a github repository
    #locate folder using: cd "folder name"
    #once located the folder, write: git init
    #to upload: git add .
        # '.' uploads everything
    #write: git status --> Tells you what files have been added
    #write: git commit -m "__(insert name)__"
        #e.g. git commit -m "first commit"
    #To upload to the repository: git push --set-upstream "_(insert URL)_" master
    
#To download files to the folder you selected: git clone

#Changing content of a file: 
    #1. Locate Folder
    #2. write: git status (if name is red & highlighted = means it is edited)
    #3. git add .
    #3. 
    
    
    


        
        
        
        
    

    