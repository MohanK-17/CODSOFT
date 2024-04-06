import string
import random
import tkinter as tk
from tkinter import messagebox

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

def generate_and_display_password():
    length = length_entry.get()
    complexity = complexity_var.get()
    
    try:
        length = int(length)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for password length.")
        return
    
    if complexity == "Normal":
        include_digits = False
        include_letters = True
        include_special_chars = False
    elif complexity == "Medium":
        include_digits = True
        include_letters = True
        include_special_chars = False
    elif complexity == "High":
        include_digits = True
        include_letters = True
        include_special_chars = True
    
    password = generate_password(length, include_digits, include_letters, include_special_chars)
    result_label.config(text="Generated Password: " + password)

# Create GUI
root = tk.Tk()
root.title("Password Generator")

# Password Length
length_label = tk.Label(root, text="Enter password length:")
length_label.grid(row=0, column=0, padx=5, pady=5)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=5, pady=5)

# Complexity Level
complexity_label = tk.Label(root, text="Choose password complexity level:")
complexity_label.grid(row=1, column=0, padx=5, pady=5)
complexity_var = tk.StringVar(root)
complexity_var.set("Normal")
complexity_optionmenu = tk.OptionMenu(root, complexity_var, "Normal", "Medium", "High")
complexity_optionmenu.grid(row=1, column=1, padx=5, pady=5)

# Generate Button
generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password)
generate_button.grid(row=2, columnspan=2, padx=5, pady=5)

# Result Label
result_label = tk.Label(root, text="")
result_label.grid(row=3, columnspan=2, padx=5, pady=5)

root.mainloop()
