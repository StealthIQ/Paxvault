# Paxvault

Paxvault is a command line offline password manager written in Python. It is an open source project that provides a secure and convenient way to manage your passwords. With its AES-256 encryption and various password management modules, Paxvault ensures the utmost security for your sensitive information.
## Demo

[![PaxVault CLI
demo](https://asciinema.org/a/do4mrvnSGnbP01PjuvENwc54h.svg)](https://asciinema.org/a/do4mrvnSGnbP01PjuvENwc54h?autoplay=1)

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

1. **Check Python Version**: Ensure you have the latest Python version installed:
   ```bash
   python3 --version
   ```

2. **Clone and Install**: Clone the repository, navigate to the project folder, and install the required libraries:
   ```bash
   git clone https://github.com/StealthIQ/Paxvault.git
   cd Paxvault/
   pip install -r requirements.txt
   ```

3. **Linux Users**: For Linux users, streamline the package installation process:
   ```bash
   while IFS= read -r line; do pip install "$line"; done < requirements.txt
   ```

4. **MySQL Installation**: For Arch Linux users, install MySQL server using `paru`:
   ```shell
   paru -Sy mysql
   mysql --version
   ```
   
   For other operating systems, ensure to download the appropriate packages using your package manager.
## Troubleshooting 

### MySQL Login and Permissions
- **Login to MySQL**: Access MySQL database:
  ```bash
  sudo mysql -u root -p
  ```

- **Check User Permissions**: Verify user permissions:
  ```sql
  SHOW GRANTS FOR 'root'@'localhost'; 
  ```

- **Grant Permissions**: Grant necessary permissions to users:
  ```sql
  GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION;
  ```

### Password Reset
1. **Stop MySQL**: Stop MySQL service:
   ```bash
   sudo systemctl stop mariadb
   ```

2. **Start in Safe Mode**: Start MariaDB in Safe Mode to reset the root user password:
   ```bash
   sudo mysqld_safe --skip-grant-tables &
   ```

3. **Open New Terminal**: Open a new terminal window and access MySQL:
   ```bash
   mysql -u root 
   ```

4. **Reset Password**: Reset the password using one of the following methods:
   - Using `UPDATE` command:
     ```sql
     USE mysql;
     UPDATE user SET authentication_string=PASSWORD('new_password') WHERE User='root';
     FLUSH PRIVILEGES;
     ```
   - Using `ALTER USER` command:
     ```sql
     ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password';
     ```
   - Using `UPDATE` command (for older MySQL versions):
     ```sql
     UPDATE user SET password=PASSWORD('new_password') WHERE User='root';
     ```

   Replace `'new_password'` with your desired password or set it to default `'root'`.

5. **Exit MySQL**: Exit MySQL:
   ```sql
   exit;
   ```

6. **Stop Safe Mode**: Stop MySQL Safe Mode:
   ```bash
   sudo systemctl start mariadb
   ```

7. **Restart Service**: Restart the MySQL service:
   ```bash
   sudo systemctl start mysqld
   ```

## Initialize MySQL

To initialize MySQL in your system:

```bash
sudo mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/mysql
```

Start the MySQL service:

```bash
sudo systemctl start mysqld
```

#### **Run Main Script**: 
- Finally, run the main script to start using Paxvault:
   ```bash
   python3 main.py
   ```

## Roadmap

- [ ] Fix minor bugs
- [ ] SQL DB Schema 
- [ ] haveibeenpwned API ratelimit
## Project Creation Process

1. **Project Mind Map** 
![Imgur](https://i.imgur.com/vk8z0x7.png)

- Here I will provide a brief explanation of how I developed this project, the challenges I faced, and what I have learned so far.

## Feedback

If you have any feedback, please reach out to me at stealthiq[at]protonmail.com or [twitter](https://twitter.com/StealthIQQ)


## Authors

- [@Stealthiq](https://www.github.com/stealthiq)
