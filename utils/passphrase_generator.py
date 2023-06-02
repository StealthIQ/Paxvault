import os
import time 
import secrets
import random
import string
import pyperclip
from random_word import RandomWords
from rich import print
from rich.prompt import Prompt
from time import perf_counter

# Setting input as Prompt.ask
input = Prompt.ask

# Main Function
def passphrase_main():
    # os.system("clear||cls")
    passphrase_menu = ("""[purple]   :rocket: Passphrase Generator 1.0[yellow]

    [0] - Your Own Custom Passphrase 
    [1] - Complexity lev I   (Just Random Words)
    [2] - Complexity lev II  (lev I + Capitalization)
    [3] - Comlexity lev III (lev II + Numbers)
    [4] - Complexity lev IV  (lev III + Symbols)
    [B] - Main Menu
          """)

    print(passphrase_menu)
    user_choice = input("[purple]   :rocket:[red] Enter your choice ")
    choice_handler = ChoiceHandler()
    choice_handler.handle_choice(user_choice)

# User Choice Class
class ChoiceHandler:
    def __init__(self):
        self.options = {"1", "2", "3", "4", "0"}
    def handle_choice(self, choice):
        if choice.lower() == "b":
            exit()
        elif choice not in self.options:
            print("[red]Invalid Option!")
            time.sleep(1)
            passphrase_main()
        elif int(choice) == 0:
            passphrase_generator = PassphraseGenerator(0)
            _passphrase_ = passphrase_generator.lev_0_custom_passphrase()
            print("[bright_cyan]   :envelope:  [bright_white]Your Passphrase is :", _passphrase_)
            copy_to_clipboard(_passphrase_)
        else:
            num_words = input("[purple]   :question:[bright_white] Enter the number of words [blue]")

            start = perf_counter() 
            passphrase_generator = PassphraseGenerator(num_words)

            choices = {
                "1": passphrase_generator.lev_1_passphrase,
                "2": passphrase_generator.lev_2_passphrase,
                "3": passphrase_generator.lev_3_passphrase,
                "4": passphrase_generator.lev_4_passphrase,
                "0": passphrase_generator.lev_0_custom_passphrase
            }
            _passphrase_lev = choices.get(choice)
            if _passphrase_lev is not None:
                _passphrase_ = _passphrase_lev()
                print("[bright_cyan]   :envelope:  [bright_white]Your Passphrase is :", _passphrase_)
                stop = perf_counter()
                print("[blue]   :clock2: Time Taken :", stop-start)
                copy_to_clipboard(_passphrase_)

class PassphraseGenerator:
    def __init__(self, num_words):
        self.num_words = num_words
        self.list_random_words = []

    def generate_random_word(self, custom=False, custom_word=""):
        if custom:
            return custom_word
        else:
            return RandomWords().get_random_word()

    def capitalize_word_at_index(self, word, index):
        return word[:index] + word[index].upper() + word[index+1:]

    def insert_numbers(self, word, numbers, index):
        word_list = list(word)
        for i, num in enumerate(numbers):
            word_list.insert(index+1, num)
            index += 1
        return ''.join(word_list)

    def insert_symbols(self, word, symbols, index):
        word_list = list(word)
        for i, sym in enumerate(symbols):
            word_list.insert(index+1, sym)
            index += 1
        return ''.join(word_list)

    def lev_1_passphrase(self):
        for _ in range(int(self.num_words)):
            one_random_word = self.generate_random_word()
            self.list_random_words.append(one_random_word)
        return ' '.join(self.list_random_words)

    def lev_2_passphrase(self, custom=False, custom_word=""):
        for _ in range(int(self.num_words)):
            one_random_word = self.generate_random_word(custom, custom_word)
            len_words = len(one_random_word)
            index = secrets.randbelow(len_words)
            capitalized_word = self.capitalize_word_at_index(one_random_word, index)
            self.list_random_words.append(capitalized_word)
        return ' '.join(self.list_random_words)

    def lev_3_passphrase(self):
        for _ in range(int(self.num_words)):
            self.numbers = secrets.choice(string.digits)
            one_random_word = self.generate_random_word()
            len_words = len(one_random_word)
            index = secrets.randbelow(len_words)
            capitalized_word = self.capitalize_word_at_index(one_random_word, index)
            num_passphrase = self.insert_numbers(capitalized_word, self.numbers, index)
            self.list_random_words.append(num_passphrase)
        return ' '.join(self.list_random_words)

    def lev_4_passphrase(self):
        for _ in range(int(self.num_words)):
            one_random_word = self.generate_random_word()
            len_words = len(one_random_word)
            index = secrets.randbelow(len_words)
            capitalized_word = self.capitalize_word_at_index(one_random_word, index)
            self.numbers = secrets.choice(string.digits)
            num_passphrase = self.insert_numbers(capitalized_word, self.numbers, index)
            self.symbols = secrets.choice(string.punctuation)
            sym_passphrase = self.insert_symbols(num_passphrase, self.symbols, index)
            self.list_random_words.append(sym_passphrase)
        return ' '.join(self.list_random_words)

    def lev_0_custom_passphrase(self):
        num_words = int(input("[purple]   :question:[bright_white] Enter the number of custom words you want to add "))
        
        capitalized_pwd = input("[purple]   :key:[bright_white] Add Capitalization (y/n) ").lower() == "y"
        num_passphrase = input("[purple]   :key:[bright_white] Add Numbers (y/n) ").lower() == "y"
        sym_passphrase = input("[purple]   :key:[bright_white] Add Symbols (y/n) ").lower() == "y"
        print("")

        word_list = []

        for i in range(num_words):
            custom_word = input(f"[purple]   :question:[bright_white] Enter the word ({i+1}) ")

            if sym_passphrase and capitalized_pwd and num_passphrase:
                index = secrets.randbelow(len(custom_word))
                capitalized_word = self.capitalize_word_at_index(custom_word, index)
                self.numbers = secrets.choice(string.digits)
                num_passphrase = self.insert_numbers(capitalized_word, self.numbers, index)
                self.symbols = secrets.choice(string.punctuation)
                sym_passphrase = self.insert_symbols(num_passphrase, self.symbols, index)
                word_list.append(sym_passphrase)

            elif sym_passphrase and capitalized_pwd:
                index = secrets.randbelow(len(custom_word))
                capitalized_word = self.capitalize_word_at_index(custom_word, index)
                symbols = secrets.choice(string.punctuation)
                sym_passphrase = self.insert_symbols(capitalized_word, symbols, index)
                word_list.append(sym_passphrase)

            elif sym_passphrase and num_passphrase:
                index = secrets.randbelow(len(custom_word))
                numbers = secrets.choice(string.digits)
                num_passphrase = self.insert_numbers(custom_word, numbers, index)
                symbols = secrets.choice(string.punctuation)
                sym_passphrase = self.insert_symbols(num_passphrase, symbols, index)
                word_list.append(sym_passphrase)

            elif capitalized_pwd and num_passphrase:
                index = secrets.randbelow(len(custom_word))
                capitalized_word = self.capitalize_word_at_index(custom_word, index)
                numbers = secrets.choice(string.digits)
                num_passphrase = self.insert_numbers(capitalized_word, numbers, index)
                word_list.append(num_passphrase)

            elif sym_passphrase:
                index = secrets.randbelow(len(custom_word))
                symbols = secrets.choice(string.punctuation)
                sym_passphrase = self.insert_symbols(custom_word, symbols, index)
                word_list.append(sym_passphrase)

            elif capitalized_pwd:
                index = secrets.randbelow(len(custom_word))
                capitalized_word = self.capitalize_word_at_index(custom_word, index)
                word_list.append(capitalized_word)

            elif num_passphrase:
                index = secrets.randbelow(len(custom_word))
                numbers = secrets.choice(string.digits)
                num_passphrase = self.insert_numbers(custom_word, numbers, index)
                word_list.append(num_passphrase)

            else:
                word_list.append(custom_word)
                # pass
        randomize_order = input("\n[purple]   :question:[bright_white] Do you want to randomize the passphrase list: (y/n)").lower() == "y"
        if randomize_order:
            shuffled_list = random.shuffle(word_list)

        return ' '.join(word_list)
        

# Copr to clipboard function
def copy_to_clipboard(_passphrase_):
    copy_to_clipboard = input("[purple]   :question:[bright_white] Do you want to copy the passphrase to your clipboard (y/n)").lower() == "y"
    if copy_to_clipboard:
        pyperclip.copy(_passphrase_)
        print("\n   [green]:heavy_check_mark:  Done!! Copied passphrase to clipboard :)\n")
    input("\n  [~] Press any key to continue (")


if __name__ == "__main__":
    try:
        passphrase_main()
    except KeyboardInterrupt:
        os.system("clear||cls")
        exit()
