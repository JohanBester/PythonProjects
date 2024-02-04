# guessNumber.py
from asyncio.windows_events import NULL
import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    guess_count = 0

    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x} : "))
        guess_count += 1

        if guess < random_number:
            print("Sorry, guess again, to low.")
        else:
            print("Sorry, guess again, to high.")

    print(f"\nYeaaaaaah!!! Congrats, you guessed {random_number} correctly!")
    print(f"You took only {guess_count} tries!")


def computer_guess(x):
    low = int(1)
    high = int(x)+1
    guess = 0
    feedback = ""
    computer_guesses = 0

    while feedback != "c":
        computer_guesses = computer_guesses + 1
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = high

        feedback = input(
            f"\nIs {guess} too hight (H), too low (L) or correct (C)?").lower()

        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        elif feedback != "c":
            print("\nSorry, I did not understand your response. Please try again.")
            continue

    print(
        f"\nYeaaaaaah!!! The computer guessed your number, {guess}, correctly!")
    print(f"The computer took only {computer_guesses} guesses.")


answer1 = ""
answer1 = input("Shall we play a number-guessing game? (yes/no) ").lower()

while answer1 != "":
    if "y" in answer1:
        answer2 = input("Do you want to pick a number for the computer to guess?: (yes/no)").lower()
        if "y" in answer2:
            print("Great! Pick a number between 0 and 1000. Keep it secret!")
            print("Let's see how many guesses the computer needs to guess your number")
            computer_guess(1000)
        else:
            print("OK. I'll pick a number and you guess!")
            guess(15)
    elif "n" in answer1:
        break
    else:
        print("\nSorry, I did not understand your response. Please try again.")
        answer1 = ""
        continue
    
    answer1 = input("Shall we play again? (yes/no) ").lower()

print("OK, bye!")
