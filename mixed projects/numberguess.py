# numberguess.py
import random

num = random.randint(1, 15)
guess = None

while guess != num:
    guess = input("guess a number between 1 and 15: ")
    guess = int(guess)

    if guess == num:
        print("congratulations! you won!")
        break
    else:
        print("nope, sorry. try again!")
