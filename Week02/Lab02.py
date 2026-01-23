#"Rock", "Paper", "Scissor"

# Minimum of two users! 

import random
choice = ["Rock", "Paper", "Scissor"]

playerChoice = input("Choose a number between the following list:  1.Rock, 2.Paper, 3.Scissors: ")

playerChoice =int(playerChoice)

#Input Check
if playerChoice <1 or playerChoice > 3:
    print ("Erro: You should chose a number between 1 and 3!")
else:
    #Develop the game logic throug if/elif/else
    computerChoice = random.randint(1, 3)

    if playerChoice == computerChoice:
        print("It's a tie!")
    elif playerChoice == 1 and computerChoice == 3:
        print("Rock beats Scissor -You win!")
    elif playerChoice == 2 and computerChoice == 1:
        print("Paper beats Rock - You win!")
    elif playerChoice == 3 and computerChoice == 2:   
        print("Scissor beats Paper - You win")
    else:
        print("You Lose")    

