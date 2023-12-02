import random

def get_user_choice():
    while True:
        print("Choose your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        choice = input("Enter your choice (1/2/3): ")

        if choice in ["1", "2", "3"]:
            return choice
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def get_computer_choice():
    return str(random.randint(1, 3))

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "1" and computer_choice == "3") or \
         (user_choice == "2" and computer_choice == "1") or \
         (user_choice == "3" and computer_choice == "2"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    user_score = 0
    computer_score = 0

    print("Rock-Paper-Scissors Game")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"User Score: {user_score}")
        print(f"Computer Score: {computer_score}")

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
