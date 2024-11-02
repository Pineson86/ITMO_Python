import string
import random

password_length = 12

def password_generator(password_length):
    chars = string.printable
    password = ''.join(random.choices(chars, k=password_length))
    return password
print(password_generator(password_length))