import random

options = ("rock", "paper", "scissors")
# we are not going to change the options so we can use a tuple

running = True

while running:
    player = None
    computer = random.choice(options)

    # Input validation
    while player not in options:
        player = input("Enter rock, paper or scissors: ").lower()
        if player not in options:
            print("Invalid choice, please try again.")

    # Game logic
    print("Computer chose:", computer)
    print("Player chose:", player)

    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("You lose!")

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        running = False
        print("Thanks for playing!")
