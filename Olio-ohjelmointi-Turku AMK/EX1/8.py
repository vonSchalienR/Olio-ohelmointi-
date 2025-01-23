import random

def get_user_choice():
    """
    Reads the user's choice and validates it.
    Returns 'rock', 'paper', or 'scissors'.
    """
    choices = ["rock", "paper", "scissors"]
    while True:
        user_input = input("Enter your choice (rock, paper, scissors): ").strip().lower()
        if user_input in choices:
            return user_input
        else:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    """
    Randomly generates the computer's choice.
    Returns 'rock', 'paper', or 'scissors'.
    """
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    """
    Determines the winner of a single round.
    Returns 'user', 'computer', or 'tie'.
    """
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    """
    Plays the Rock-Paper-Scissors game until either the user or the computer gets 3 wins.
    """
    user_wins = 0
    computer_wins = 0

    print("Welcome to Rock-Paper-Scissors! First to 3 wins is the winner.")

    while user_wins < 3 and computer_wins < 3:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        
        if result == "user":
            user_wins += 1
            print("You win this round!")
        elif result == "computer":
            computer_wins += 1
            print("Computer wins this round!")
        else:
            print("It's a tie!")

        print(f"Score - You: {user_wins}, Computer: {computer_wins}\n")

    # Announce the final winner
    if user_wins == 3:
        print("Congratulations! You won the game!")
    else:
        print("Computer won the game. Better luck next time!")

# Start the game
play_game()
