import random

def get_guess():
    guess = input("Enter your guess (1–20): ")
    try:
        user_guess = int(guess)
        if user_guess < 1 or user_guess > 20:
            return None
        else:
            return user_guess
    except ValueError:
        return None


def main():
    print("=== Number Guessing Game ===")

    while True:
        print("I'm thinking of a number between 1 and 20...")
        secret_number = random.randint(1, 20)
        attempts = 0

        while True:
            user_guess = get_guess()

            if user_guess is None:
                print("Invalid input. Please enter a number between 1 and 20.\n")
                continue

            attempts += 1

            if user_guess > secret_number:
                print("Too high!\n")
            elif user_guess < secret_number:
                print("Too low!\n")
            else:
                print(f"Correct! You guessed it in {attempts} attempts.\n")
                break  # end round

        # Ask if player wants to play again
        while True:
            again = input("Play again? (y/n): ").strip().lower()
            if again == "y":
                print()
                break  # start new round
            elif again == "n":
                print("Goodbye!")
                return  # exit entire game
            else:
                print("Invalid choice. Please enter 'y' or 'n'.\n")

if __name__ == "__main__":
    main()
