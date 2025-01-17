"""
This script generates a random password based on user-defined criteria such as length and character types.
It also provides an option to save the generated password to a file.
"""
import time # for delay
import random # for random character selection
import os #for clearing the screen
import string # for characters
import base64 # for encoding and decoding

uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
symbols = string.punctuation
numbers = string.digits
password_characters = uppercase_letters + lowercase_letters + symbols + numbers

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print("Welcome! This is a password generator created by _stealthy.")
time.sleep(0.5)
input("Press any key to continue...")
clear()
time.sleep(1)

while True:
    try:
        password_length = int(input("What is the character limit you want to have in your password?: "))
        clear()
        time.sleep(1)   
        if password_length > 0:
            break
        else:
            print("Please enter a positive integer.")
            clear()
    except ValueError:
        print("Please enter a valid integer.")
        clear() 

password_generated = False # flag to check if password is generated

while True:
    time.sleep(0.5)
    loop_question = input("Do you wish to generate a password?(y/n): ")
    if loop_question == 'y':
        password = "".join(random.sample(password_characters, password_length))
        clear()
        for i in range(4):
            print(f"Creating password{'.' * i}")
            time.sleep(1)
            clear()
        print("Your password is: ", end='', flush=True)
        time.sleep(0.5)
        print(password)
        password_generated = True # password is generated
    elif loop_question == "n":
        clear()
        time.sleep(1)
        break
    else:
        print(loop_question, " is not a valid response")
        time.sleep(1)
        clear()

while password_generated is True:
    save_question = input("Do you wish to save your password?(y/n): ")
    if save_question == "y":
        if not os.path.exists('password_saves'):
             os.makedirs('password_saves')
        with open('password_saves/passwords.txt', 'a') as file:
                file.write(password + '\n')
        print("Password saved successfully.")
        time.sleep(1)
        clear()
        break
    elif save_question == "n":
        clear()
        break
    else:
        print(save_question, " is not a valid response")
        time.sleep(1)
        clear()