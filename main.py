import os
import arts
# from utils.just_banner import *
import getpass
import time
import webbrowser
from datetime import datetime
# Sub Folder Lib--------------------------------------
from utils.password_quality_meter import Main_checker
from utils.password_generator import password_generator
from utils.passphrase_generator import passphrase_main
from utils.sql_database import Passfx_Users_Add, Passfx_login_verify, sql_db_setting
from utils.password_manager import pass_manager_main
# Rich Console Color Lib------------------------------
from rich.prompt import Prompt
from rich import print
# Hashing Libs----------------------------------------
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# Get the current date and time
date_time_now = datetime.now()

# Format the date and time string
formatted_date_time = date_time_now.strftime("%d-%m-%Y %H:%M:%S")
date_created = formatted_date_time

# Define a function to encrypt a password using AES-256 encryption
def encrypt_password(password, key):
    # Hash the key with SHA-256
    hashed_key = hashlib.sha256(key.encode()).digest()

    # Initialize the AES cipher with the hashed key
    cipher = AES.new(hashed_key, AES.MODE_CBC)

    # Pad the password using the new padding method
    block_size = AES.block_size
    pad_size = block_size - len(password.encode()) % block_size
    padding = bytes([pad_size] * pad_size)
    padded_password = password.encode() + padding

    # Encrypt the padded password
    encrypted_password = cipher.encrypt(padded_password)

    # Return the encrypted password and the initialization vector
    return encrypted_password, cipher.iv.hex()

# Define a function to decrypt an encrypted password using AES-256 encryption
def decrypt_password(encrypted_password_hex, key, iv):
    # To convert a hex string back to its original bytes form
    encrypted_password = bytes.fromhex(encrypted_password_hex)
    # Hash the key using SHA-256
    hashed_key = hashlib.sha256(key.encode()).digest()

    # Initialize the AES cipher with the hashed key and the initialization vector
    cipher = AES.new(hashed_key, AES.MODE_CBC, iv=bytes.fromhex(iv))

    # Decrypt the encrypted password
    decrypted_password = cipher.decrypt(encrypted_password)

    # Unpad the decrypted password using the new unpadding method
    pad_size = decrypted_password[-1]
    unpadded_password = decrypted_password[:-pad_size].decode()

    # Return the decrypted password
    return unpadded_password


def Main_modules(username):
    try:
        while True:
            arts.banner()
            arts.Main_modules()
            choice = Prompt.ask(f'[yellow]    Enter your choice → [/yellow]')
            if choice == '1':
                arts.banner()
                pass_manager_main(username)
            elif choice == '2':
                arts.banner()
                password_generator()
                # time.sleep(4)
            elif choice == '3':
                arts.banner()
                passphrase_main()
            elif choice == '4':
                arts.banner()
                Main_checker()
            elif choice == "Q" or choice == "q":
                exit()
            elif choice == "B" or choice == 'b':
                main()
            else:
                print(f'[red]\t ⚠ Invalid choice.')
    except KeyboardInterrupt:
        os.system("clear||cls")
        exit()


# Function to login a user
def login():
    arts.banner()
    username = Prompt.ask('\t[x] Enter your username')
    password = getpass.getpass(prompt='\t[x] Enter the password :', stream=None)
    username_query_value = Passfx_login_verify(username)

    if username_query_value is not None and username in username_query_value[1]:
        hashed_pwd = decrypt_password(username_query_value[4], username_query_value[1], username_query_value[5])
        if password.strip() == hashed_pwd.strip():
            print(f'\t[green]✓  Login successful!')
            time.sleep(2)
            Main_modules(username)
        else:
            arts.banner()
            print(f'\t[red] ⚠  Invalid password.')
            time.sleep(2)
    else:
        arts.banner()
        print(f'\t[red] ⚠  Invalid username or password.')
        time.sleep(2)


# Function to register a new user
def register():
    arts.banner()
    username = Prompt.ask('\t[x] Enter a username')
    email = Prompt.ask('\t[x] Enter your email adress')
    main_key = username
    password = getpass.getpass(prompt='\t[x] Enter the password :', stream=None).strip()
    re_password = getpass.getpass(prompt='\t[x] Renter the password :', stream=None).strip()
    
    encrypted_password, cipher_iv_password = encrypt_password(password, main_key)
    encrypted_email, cipher_iv_email = encrypt_password(email, main_key)



    if password == re_password:
        Passfx_Users_Add(username, main_key, encrypted_email.hex(), cipher_iv_email, encrypted_password.hex(), cipher_iv_password, date_created)
        print(f'\n\t[green]✓  User successfully registered!')
        time.sleep(2)
    else:
        arts.banner()
        print(f"\t[red] ⚠  Passsword Incorrect, try again...")
        time.sleep(2)
        register()


# Main function to prompt user to register or login
def main():
    try:
        while True:
            arts.banner()
            arts.Start_modules()
            choice = Prompt.ask(f'[yellow]    Enter your choice → ')
            if choice == '1':
                login()
            elif choice == '2':
                register()
            elif choice == '3':
                arts.banner()
                sql_db_setting()
            elif choice == '4':
                webbrowser.get('firefox').open('https://github.com/StealthIQ')
            elif choice == "q":
                exit()
            else:
                print(f'[red]\t ⚠ Invalid choice.')
    except KeyboardInterrupt:
        os.system("clear||cls")
        exit()

if __name__ == '__main__':
    main()


