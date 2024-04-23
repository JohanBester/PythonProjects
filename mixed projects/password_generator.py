import random
import string
import math
import re

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation
all_chars = lowercase + uppercase + digits + symbols 
all_chars *= 4

DEFAULT_LENGTH = 8


def check_password_strength(password):
    score = 0
    
    # Check length
    if len(password) >= 8:
        score += 1
    elif len(password) >= 16:
        score += 2
    
    # Check for uppercase letters
    if re.search("[A-Z]", password):
        score += 1
    
    # Check for lowercase letters
    if re.search("[a-z]", password):
        score += 1
    
    # Check for numbers
    if re.search("[0-9]", password):
        score += 1
    
    # Check for special characters
    if re.search("[!@#$%^&*()_+=\-[\]{};:'\"|,.<>/?]", password):
        score += 1
    
    # Evaluate score and give feedback
    if score >= 5:
        return "Very Strong"
    elif score == 4:
        return "Strong"
    elif score == 3:
        return "Medium"
    elif score == 2:
        return "Weak"
    else:
        return "Very Weak"


def estimate_crack_time(password):
    # Determine character set used in the password
    used_characters = set()
    for char in password:
        if char in lowercase:
            used_characters.add('lowercase')
        elif char in uppercase:
            used_characters.add('uppercase')
        elif char in digits:
            used_characters.add('digits')
        elif char in symbols:
            used_characters.add('symbols')
    
    # Calculate the number of possible characters used
    total_characters = len(lowercase + uppercase + digits + symbols)
    used_character_count = sum(1 for char_set in used_characters)
    
    # Calculate the entropy and time to crack
    entropy = math.log(total_characters, 2) * len(password)
    
    # Assume 10 billion guesses per second as a baseline
    guesses_per_second = 1e10
    
    # Calculate time to crack in seconds
    time_to_crack_seconds = (2 ** entropy) / guesses_per_second
    
    # Convert time to crack to more readable format
    time_units = [('seconds', 60), ('minutes', 60), ('hours', 24), ('days', 365), ('years', 100)]
    for unit, factor in time_units:
        if time_to_crack_seconds < factor:
            break
        time_to_crack_seconds /= factor
    else:
        unit = 'centuries'
    
    return time_to_crack_seconds, unit


# Get password length
psLength = input("Enter a number larger than 5 for the required password length : ")
try:
    number = int(psLength)
    if number < 6:
        psLength = input("Enter a number larger than 5 for the required password length : ")
    elif number >= 6:
        DEFAULT_LENGTH = number
except ValueError:
    print(f"{psLength} is not an integer.")
    exit()


# Generate new password
password = ''.join(random.sample(all_chars, DEFAULT_LENGTH))
print('\n')
print('Generated Password: ', password)

# Check password strength
password_strength = check_password_strength(password)
print(f"Password strength: {password_strength}")

# Estimate time to crack the password
time_to_crack_seconds, unit = estimate_crack_time(password)
print(f"Estimated time to crack the password: {time_to_crack_seconds:.2f} {unit}")
