def rock_paper_scissors():
import random

print('''Welcome to NOVACHRONO\'s arcade.
Let\'s play a game of rock, paper, scissors''')
game_options = ["rock", "paper","scissors"]

#Ask User for input
user_choice = input('What do you choose? Type "R" for Rock, "P" for Paper or "S" for Scissors. \n')

#Computer's choice
computer_choice = random.choice(game_options)

# INPUT CONDITIONAL STATEMENTS FOR USER AND COMPUTER CHOICE
if user_choice == "R" or "r":
    print("You chose rock.")
    if computer_choice == "rock":
        print("Computer chose rock")
        print('It\'s a draw')
    elif computer_choice == "paper":
        print("Computer chose paper")
        print("You lose")
    else:
        print("Computer chose scissors")
        print("You win")



elif user_choice == "P" or "p":
    print("You chose paper.")
    if computer_choice == "rock":
        print(f"Computer chose rock")
        print("You win")
    elif computer_choice == "paper":
        print("Computer chose paper")
        print('It\'s a draw')
    else:
        print("Computer chose scissors")
        print("You lose")



elif user_choice == "S" or "s":
    print("You chose scissors.")
    if computer_input == "rock":
        print("Computer chose scissors")
        print("You win")
    elif computer_input == "paper":
        print("Computer chose paper")
        print("You lose")
    else:
        print("Computer chose scissors")
        print('It\'s a draw')

else:
    print("Error: Out of range")

#Ask if user will love to continue
game_choice = input("Would you like to play again? Type "Y" for yes and "N" for no /n")
while game_choice == "Y" or "y":
    rock_paper_scissors()
else:
	print("Thank you for playing")
break
