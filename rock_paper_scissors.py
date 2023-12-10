from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
intro = """
************************************************************************************************

ROCK PAPER SCISSORS
This is game of Rock, Paper, Scissors!
There will be 3 rounds in which you will enter your move and then the computer will make their move.
It's simple: rock beats scissors, scissors beats paper and paper beats rock. 
Good luck! May the best player win!

***********************************************************************************************
"""
print(rock + paper + scissors)
print(intro)

# Best of 3 game
games = 0
player_wins = 0
comp_wins = 0

while games < 3:
    # Pick a random number from 1 to 3
    num = randint(1,4)

    # Turn that random number into the computer's RPS move
    if num == 1:
        comp_move = "rock"
    elif num == 2:
        comp_move = "paper"
    else:
        comp_move = "scissors"

    # Ask a user to enter their move
    player_move = input("enter your move: ")
    player_move = player_move.lower()

    # Print the rock, paper, or scissors ASCII art that corresponds to the player's move
    print("Your move:")
    if player_move == "rock":
        print(rock)
    elif player_move == "paper":
        print(paper)
    elif player_move == "scissors":
        print(scissors)
    else:
        print("Sorry, that's not a valid move")

    # Print the rock, paper, or scissors ASCII art that corresponds to the computer's move
    print("Computer's move:")
    if comp_move == "rock":
        print(rock)
    elif comp_move == "paper":
        print(paper)
    else:
        print(scissors)

    # Figure out who wins and print the result!
    if player_move == comp_move:
        player_wins += 0
        comp_wins += 0
    elif (player_move=="rock" and comp_move == "scissors") or (player_move=="paper" and comp_move=="rock") or player_move == "scissors" and comp_move=="paper":
        player_wins +=1
    else:
        comp_wins += 1
    print(f"Player {player_wins}, Computer {comp_wins}")
    games += 1

    print("\n ************************************************************************************************ z\n")

# Figure out who wins overall and print the result!
if player_wins > comp_wins:
    print("****YOU WIN!****")
elif player_wins < comp_wins:
    print("****COPUTER WINS!****")
else:
    print("****IT'S A DRAW****")
