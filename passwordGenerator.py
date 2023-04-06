#! /usr/bin/env python3

# Welcome to my password Generator!

import random
import string
import pyperclip

passwordLen = input("Enter the desired password length: ")

def generate_password(length=int(passwordLen)):
    password = []
    for _ in range(length):
        choice = random.choices(
            [getNumber(), getLetter(), getCharacter()], 
            weights=[3, 5, 2], # Increase weights to increase frequency of a character
            k=1
        )
        password.append(choice[0])
    return ''.join(password)

def getNumber():
    return random.choice(string.digits)

def getLetter():
    return random.choice(string.ascii_letters)

def getCharacter():
    return random.choice('!#$&*?!')

password = generate_password()
print("Your password has been copied to your clipboard!")
pyperclip.copy(password)
