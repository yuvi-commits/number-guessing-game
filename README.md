# 🎯 Number Guessing Game

A simple command-line game written in Python. The computer picks a random number between 1 and 100, and you have 7 attempts to guess it correctly. After each guess, you're told whether to go higher or lower.

## How to run

1. Make sure you have Python 3 installed.
2. Clone this repo or download `guess_the_number.py`.
3. Run it from your terminal:

   ```bash
   python guess_the_number.py
   ```

4. Enter your guesses when prompted!

## Example

```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 7 attempts. Good luck!

Attempt 1/7 — Your guess: 50
Too high! Try a lower number.

Attempt 2/7 — Your guess: 25
Too low! Try a higher number.
...
🎉 Correct! You guessed it in 4 attempt(s).
```

## What I learned building this

- Using Python's `random` module
- Loops and conditionals (`while`, `if`/`elif`/`else`)
- Handling and validating user input
- Structuring code with functions

## Possible improvements

- [ ] Add difficulty levels (change range / attempts)
- [ ] Track and display best score across games
- [ ] Add a hint system ("getting warmer/colder")
