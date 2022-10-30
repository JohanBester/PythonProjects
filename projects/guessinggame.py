# guessinggame.py

import random
from words import words
import string


def get_valid_word(words):
     # randomly chooses something from the list
     word = random.choice(words)
     while '-' in word or ' ' in word or (len(word) < 5):
          word = random.choice(words)
     return word.upper()

secret_word = get_valid_word(words)
print(secret_word)
word_start = secret_word[0]
word_end = secret_word[-1]

def letter_hint(secret_word):
     wordLength = len(secret_word)-1
     ranNum = random.randrange(0, wordLength)
     random_letter = secret_word[ranNum]
     return random_letter

guess = ""
guess_count = 1
guess_limit = 9
out_of_guesses = False

print("Let's play a word guessing game!")
print(f"The word starts with {word_start}.")
guess = input("Enter a guess: ").upper()

while guess != secret_word and not(out_of_guesses):
     print(f"Guess {guess_count} out of {guess_limit}.")
     
     if guess_count == 6:
          print(f"\nThe word ends with {word_end}.")
     elif guess_count > 3:
          print(f"\nThe word contains ... " + letter_hint(secret_word) + ".")
     
     if guess_count < guess_limit:
          print(f"Try again.")
          guess = input("Enter a guess: ").upper()
          guess_count += 1
     else:
          out_of_guesses = True
          break     

if out_of_guesses:
     print("\nSorry, You Lose!")
     print(f"\nThe secret word was ... {secret_word}")
else:
     print("\nCongratulations! You Win!!!!")
