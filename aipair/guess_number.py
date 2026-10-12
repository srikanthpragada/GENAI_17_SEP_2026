import random


def play_guessing_game():
    secret_number = random.randint(1, 20)
    chances = 3

    print("Guess the number between 1 and 20.")

    for attempt in range(1, chances + 1):
        while True:
            try:
                guess = int(input(f"Chance {attempt}/{chances}: "))
            except ValueError:
                print("Please enter a whole number.")
                continue

            if 1 <= guess <= 20:
                break

            print("Enter a number between 1 and 20.")

        if guess == secret_number:
            print("You guessed it!")
            return

        print("Incorrect.")

    print(f"Game over. The number was {secret_number}.")


if __name__ == "__main__":
    play_guessing_game()