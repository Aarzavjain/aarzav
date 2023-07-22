
import random

def get_user_choice():
    user_choice = input("Enter your choice (Rock, Paper, or Scissors): ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        user_choice = input("Enter your choice (Rock, Paper, or Scissors): ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "Congratulations! You win!"
    else:
        return "Sorry, you lose. Computer wins!"

def play_again():
    return input("Do you want to play again? (yes or no): ").lower() == "yes"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    play_game = True

    while play_game:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_game = play_again()

if __name__ == "__main__":
    main()
