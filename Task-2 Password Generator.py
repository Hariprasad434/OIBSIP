import random
import string
import re

def generate_password(num_digits, num_chars):
    digits = random.choices(string.digits, k=num_digits)
    characters = random.choices(string.ascii_letters + string.punctuation, k=num_chars)
    
    password = digits + characters
    random.shuffle(password)
    return ''.join(password)

def check_password_strength(password):
    if len(password) < 8:
        return "Weak (Password must be at least 8 characters long)"
    
    if (re.search(r'[A-Za-z]', password) and
        re.search(r'[0-9]', password) and
        re.search(r'[@#$%^&+=]', password)):
        return "Strong"
    else:
        return "Weak"

num_digits = int(input("Enter the number of digits: "))
num_chars = int(input("Enter the number of characters: "))

generated_password = generate_password(num_digits, num_chars)
print(f"Generated Password: {generated_password}")

user_password = input("Enter your password to check its strength: ")

strength = check_password_strength(user_password)
print(f"Your Password Strength: {strength}")
