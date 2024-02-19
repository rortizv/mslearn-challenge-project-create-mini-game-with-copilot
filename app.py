import random

options = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

while True:
    print("\n1: Rock\n2: Paper\n3: Scissors")
    player_choice = input("Choose your option (1, 2, 3): ")

    if player_choice not in ["1", "2", "3"]:
        print("Invalid option. Please choose 1, 2 or 3.")
        continue

    player_choice = options[int(player_choice) - 1]
    computer_choice = random.choice(options)

    print(f"Player chose {player_choice}, Computer chose {computer_choice}")

    if player_choice == computer_choice:
        print("It's a tie.")
    elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "paper" and computer_choice == "rock")
        or (player_choice == "scissors" and computer_choice == "paper")
    ):
        player_score += 1
        print("You won the round.")
    else:
        computer_score += 1
        print("You lost the round.")

    print(f"Score: Player - {player_score}, Computer - {computer_score}")

    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        break

print("\nThanks for playing. Final score:")
print(f"Player - {player_score}, Computer - {computer_score}")
