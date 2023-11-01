import random
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation
all_chars = lower + upper + numbers + symbols

length = 16

password = ''.join(random.sample(all_chars, length))
print('Generated Password: ', password)
