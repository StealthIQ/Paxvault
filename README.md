# Paxvault

Paxvault is a command line offline password manager written in Python. It is an open source project that provides a secure and convenient way to manage your passwords. With its AES-256 encryption and various password management modules, Paxvault ensures the utmost security for your sensitive information.

![Paxvault Screenshot](https://i.imgur.com/x2RPn8D.png)

## Features

1. **Login**
   - Secure login with username and password using SQL.

2. **Password Manager Modules**
   - **Password Manager**: Store your passwords in an encrypted database.
     - Save usernames, passwords, and emails securely.
     - Utilizes SQL database with AES-256 encryption.
     - List saved logins.
     - Auto-copy passwords to the clipboard for convenience.
   - **Password Generation**: Generate super unique and strong passwords.
     - Customize the password length.
     - Automatically capitalize characters.
     - Include numbers in the password.
     - Include symbols in the password.
     - Include emojis in the password.
     - Auto-copy generated passwords to the clipboard.
   - **Passphrase Generator**: Generate passphrases with varying complexity levels.
     - Create custom passphrases.
     - Complexity level I: Random words.
     - Complexity level II: Level I + capitalization.
     - Complexity level III: Level II + numbers.
     - Complexity level IV: Level III + symbols.
   - **Password Quality Meter**: Evaluate the strength of your passwords.
     - Perform normal checks, including minimum length, upper and lower case, numbers, and symbols.
     - Check against the [haveibeenpwned](https://haveibeenpwned.com/) database.
     - Utilize advanced password strength libraries for comprehensive checks.

## Installation

1. Make sure you have the latest version of Python installed by running the following command:
   ```bash
   python3 --version
   ```

2. Clone the repository, navigate to the project folder, and install the necessary libraries:
   ```bash
   git clone https://github.com/StealthIQ/Paxvault.git
   cd Paxvault/
   pip install -r requirements.txt
   ```

3. Run the main script to start using Paxvault:
   ```bash
   python3 main.py
   ```

## Demo

- Soon

## Roadmap

- [ ] Master brute force attack prevention in the login system.
- [ ] Implement automatic checks with [haveibeenpwned](https://haveibeenpwned.com/) to identify if your email or passwords have been involved in a data breach.

## Project Creation Process

1. **Project Mind Map** 
![Imgur](https://i.imgur.com/vk8z0x7.png)

- Here I will provide a brief explanation of how I developed this project, the challenges I faced, and what I have learned so far.

## Feedback

If you have any feedback, please reach out to me at stealthiq@protonmail.com or [twitter](https://twitter.com/StealthIQQ)


## Authors

- [@Stealthiq](https://www.github.com/stealthiq)
