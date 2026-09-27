"""
Number Guessing Game
---------------------
The computer picks a random number in a range, and you try to guess it.
After each guess, you're told if you're too high or too low.
"""

import random


def play_game():
    print("=" * 40)
    print(" Welcome to the Number Guessing Game!")
    print("=" * 40)

    # You can change this range to make the game harder/easier
    lower_bound = 1
    upper_bound = 100
    max_attempts = 7

    secret_number = random.randint(lower_bound, upper_bound)
    attempts_used = 0

    print(f"\nI'm thinking of a number between {lower_bound} and {upper_bound}.")
    print(f"You have {max_attempts} attempts. Good luck!\n")

    while attempts_used < max_attempts:
        guess_input = input(f"Attempt {attempts_used + 1}/{max_attempts} — Your guess: ")

        # Make sure the input is actually a number
        if not guess_input.strip().lstrip("-").isdigit():
            print("Please enter a valid whole number.\n")
            continue

        guess = int(guess_input)
        attempts_used += 1

        if guess < lower_bound or guess > upper_bound:
            print(f"Stay within {lower_bound}-{upper_bound}!\n")
        elif guess < secret_number:
            print("Too low! Try a higher number.\n")
        elif guess > secret_number:
            print("Too high! Try a lower number.\n")
        else:
            print(f"\n🎉 Correct! You guessed it in {attempts_used} attempt(s).")
            break
    else:
        print(f"\n💀 Out of attempts! The number was {secret_number}.")


def main():
    keep_playing = True
    while keep_playing:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        keep_playing = again == "y"

    print("\nThanks for playing! 👋")


if __name__ == "__main__":
    main()
