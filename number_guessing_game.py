#Number Guessing Game
import random
num = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))
while guess != num:
    if guess < num:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    guess = int(input("Guess a number between 1 and 10: "))
print(f"Congratulations! You guessed the number {num}.")