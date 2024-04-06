import string
import random

def generate_password(length, include_digits=True, include_letters=True, include_special_chars=True):
    characterList = ""
    
    if include_digits:
        characterList += string.digits
    if include_letters:
        characterList += string.ascii_letters
    if include_special_chars:
        characterList += string.punctuation
    
    password = []
    
    for _ in range(length):
        randomchar = random.choice(characterList)
        password.append(randomchar)
    
    return "".join(password)

def main():
    length = int(input("Enter password length: "))
    complexity = input("Choose password complexity level (normal/medium/high): ").lower()
    
    if complexity == "normal":
        include_digits = False
        include_letters = True
        include_special_chars = False
    elif complexity == "medium":
        include_digits = True
        include_letters = True
        include_special_chars = False
    elif complexity == "high":
        include_digits = True
        include_letters = True
        include_special_chars = True
    else:
        print("Invalid complexity level. Please choose from 'normal', 'medium', or 'high'.")
        return
    
    password = generate_password(length, include_digits, include_letters, include_special_chars)
    print("The random password is:", password)

if __name__ == "__main__":
    main()
