"""We are going to write a program that generates a random number and asks the user to
guess it.
If the player’s guess is higher than the actual number, the program displays “Lower
number please”. Similarly, if the user’s guess is too low, the program prints “higher
number please” When the user guesses the correct number, the program displays the
number of guesses the player used to arrive at the number."""

import random

def getnumber():
    return random.randint(1, 100)

# Generate the random number
num = getnumber()

while True:
    n = int(input("Enter your guess number: "))

    if n < num:
        print("Too low! Try a greater number.")
    elif n > num:
        print("Too high! Try a smaller number.")
    else:
        print(f"🎉 Congratulations! You guessed it right: {num}")
        break





      