import random 
import string
import pyperclip
from rich import print
import emoji

# Password Generator Function - 3x Parameter | Min Len, Numbers, Special, Emoji
def generator(min_len=8, numbers=True, special_characters=True, emojie=False, copy_to_clipboard=False):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    emoji_alias = [chr(i) for i in range(0x1F600, 0x1F699)]   
    emoji_list = ''.join(emoji_alias)

    # Setting letters as default characters
    characters = letters
    if emojie:
        characters += emoji_list
    # If number parameter = true then add digits to characters
    if numbers:
        characters += digits
    # If special_characters = true then add special to characters
    if special_characters:
        characters += special

    # Passowrd Variabel defined with 
    pwd = ""
    # Setting Default values for creteria (1)
    meet_criteria = False
    has_numbers = False
    has_special = False
    has_emoji = False

    # While not meet_criteria is False or passd len < min_len
    while not meet_criteria or len(pwd) < min_len:
        # Scrambling the password
        new_char = random.choice(characters)
        # Adding value to the pwd variable
        pwd += new_char

        # Changing default value in creteria (1)
        if new_char in digits:
            has_numbers = True
        elif new_char in special:
            has_special = True
        elif new_char in emoji_list:
            has_emoji = True

        # Setting meet_criteria to True - creteria (2)
        meet_criteria = True
        # If numbers = True 
        if numbers:
            # Both value should be True = True
            meet_criteria = has_numbers
        # If special_characters = True
        if special_characters:
            # True = True and True (Both values being True)
            meet_criteria = meet_criteria and has_special
        if emojie:
            meet_criteria = meet_criteria and has_emoji

    # Copy password to clipboard
    if copy_to_clipboard:
        pyperclip.copy(pwd)
        print("\t[red][!] Password copied to your clipboard!!")

    # Returns the password
    return pwd
    
    # Test
    print(letters, digits, special, emoji_list)


def password_generator():
    # Asking the user variable values
    try:
        min_length = int(input("\t[!] Enter the minimum length: "))
        numbers = input("\t[!] Do you want numbers (y/n): ").lower() == "y"
        special_characters = input("\t[!] Do you want special characters (y/n): ").lower() == "y"
        emojie = input("\t[!] Do you want emojis (y/n): ").lower() == "y"
        copy_to_clipboard = input("\t[!] Do you want to copy the password directly to your clipboard (y/n)").lower() == "y"
        pwd = generator(min_length, numbers, special_characters, emojie, copy_to_clipboard)
        
        # Printing the generated password 
        print("\t[red][!] The generated password is: ", pwd)
        input("\n\t[~] Press any key to continue...")

    except:
        min_length=14
        numbers = True
        special_characters = True
        copy_to_clipboard = True
        emojie = False
        print("\n\t[red][!] Generating password with default values!\n")
        
        pwd = generator(min_length, numbers, special_characters, emojie, copy_to_clipboard)
        
        # Printing the generated password 
        print("\n\t[red][!] The generated password is: ", pwd)


#--------------------------[ TESTING ]------------------------------------
if __name__ == "__main__":
    password_generator()
