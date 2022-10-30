import random
import time

def game(thing):
    
    gameList = ["rock", "paper", "scissor"]

    choice = random.choice(gameList)
    time.sleep(1)
    print(f"The users choice was {thing} and the computer chose {choice}")
    time.sleep(1)

    if thing == choice:
        print("Draw")

    elif thing == "rock" and thing != choice:
        if choice == "paper":
            print("You Lose")
        elif choice == "scissor":
            print("You Win")
    elif thing == "paper" and thing != choice:
        if choice == "rock":
            print("You Win")
        elif choice == "scissor":
            print("You Lose")
    elif thing == "scissor" and thing != choice:
        if choice == "rock":
            print("You Lose")
        elif choice == "paper":
            print("You Win")



print("Welcome to the Rock Paper Scissor game!!")
time.sleep(0.5)

gamerInput = input("Choose your weapon: ")

gamerInput = str.lower(gamerInput)

if gamerInput == "rock":
    game(gamerInput)


elif gamerInput == "paper":
    game(gamerInput)


elif gamerInput == "scissor":
    game(gamerInput)


else:
    print("Your input was false. Try again!")

