import random

choices = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Choose rock, paper, or scissors (or quit): ").lower()

    if user_choice == "quit":
        print("Thanks for playing!")
        break

    if user_choice not in choices:
        print("Invalid choice, try again.")
        continue

    computer_choice = random.choice(choices)

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
    else:
        print("Computer wins!")
