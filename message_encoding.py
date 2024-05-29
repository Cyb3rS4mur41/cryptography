
import string

def shift_character(char, shift_by):
    if char.islower():
        return chr((ord(char) - ord('a') + shift_by) % 26 + ord('a'))
    elif char.isupper():
        return chr((ord(char) - ord('A') + shift_by) % 26 + ord('A'))
    elif char.isdigit():
        return str((int(char) + shift_by) % 10)
    else:
        return char

text = input("Type the text that you would like to encode! ")
shift_by = int(input("By how many positions would you like to shift the characters? "))

new_text = ""

for char in text:
    new_char = shift_character(char, shift_by)
    new_text += new_char

print("The new text:", new_text)

