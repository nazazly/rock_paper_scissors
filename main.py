import random

def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", 0
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "You win!", 1
    else:
        return "Computer wins!", -1

def play_game():
    player_name = input("Enter your name: ")
    print(f"Welcome, {player_name}, to Rock, Paper, Scissors!")

    player_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"{player_name}, you chose {user_choice}. Computer chose {computer_choice}.")

        result, score = determine_winner(user_choice, computer_choice)
        print(result)

        if score == 1:
            player_score += 1
        elif score == -1:
            computer_score += 1

        print(f"Score - {player_name}: {player_score}, Computer: {computer_score}")

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print(f"Thanks for playing, {player_name}! Final Score - {player_name}: {player_score}, Computer: {computer_score}")
            break

if __name__ == "__main__":
    play_game()
