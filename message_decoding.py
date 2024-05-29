
import string

def shift_character(char, shift_by, decode=False):
    if char.islower():
        factor = -1 if decode else 1
        return chr((ord(char) - ord('a') + factor * shift_by) % 26 + ord('a'))
    elif char.isupper():
        factor = -1 if decode else 1
        return chr((ord(char) - ord('A') + factor * shift_by) % 26 + ord('A'))
    elif char.isdigit():
        factor = -1 if decode else 1
        return str((int(char) + factor * shift_by) % 10)
    else:
        return char

text = input("Please give me the text that you would like to decode! ")
shift_by = int(input("By how many positions was the given text shifted? "))

decoded_text = ""

for char in text:
    decoded_char = shift_character(char, shift_by, decode=True)
    decoded_text += decoded_char

print("The decoded message:", decoded_text)