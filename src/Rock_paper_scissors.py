#!/usr/bin/env python3
while True:
    playerOne = input("Please enter 0 for rock 1 for paper 2 for scissors:\n")
    playerTwo = input("Please enter 0 for rock 1 for paper 2 for scissors:\n")
    if playerOne.isdigit() and playerTwo.isdigit():
        playerOne = int(playerOne)
        playerTwo = int(playerTwo)
        if playerOne < 0 or playerOne > 2:
            print("you've entered an invalid input for player one")
        elif playerTwo < 0 or playerTwo > 2:
            print("you've entered an invalid input player two")

        else:
            break


    else:
        print("you've entered invalid input")

if (playerOne + 1) % 3 == playerTwo:
        print("Player Two won")
elif playerOne == playerTwo:
    print("It is a draw")
else:
    print("Player One won")
