import os
import time
import mysql.connector
from rich.console import Console
from rich.table import Table
from rich import print
from rich.prompt import Prompt
from datetime import datetime

input = Prompt.ask

# Get the current date and time
date_time_now = datetime.now()

# Format the date and time string
formatted_date_time = date_time_now.strftime("%d-%m-%Y %H:%M:%S")
date_created = formatted_date_time

console = Console()

def initiate_db_connection(username):
    try:
        passdb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root"
        )
        cursor = passdb.cursor()

        # Create the user db if it doesn't exist
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {username}_Database")
        cursor.execute(f"USE {username}_Database")

        return cursor, passdb    
    except mysql.connector.Error as error:
        print("Error connecting to the MySQL server:", error)

def add_data(username):
    # Creating a database for password manager
    # Connect to db
    cursor, passdb = initiate_db_connection(username)

    site_name = input("Enter the site name")
    site_url = input("Enter the site url")
    site_username_email = input("Enter the username/email used for the site")
    site_password = input("Enter the password")

    # Creating a table for the database Passfx
    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {username}_Table (
        id INT AUTO_INCREMENT PRIMARY KEY,
        site_name VARCHAR(255) NOT NULL,
        site_url VARCHAR(255) NOT NULL,
        site_username_email VARCHAR(255) NOT NULL,    
        site_password VARCHAR(255) NOT NULL,
        date_time_created VARCHAR(255)
    )
                   """)

    query = f"""
    INSERT INTO {username}_Table (site_name, site_url, site_username_email, site_password, date_time_created)
        return None, None
    VALUES (%s, %s, %s, %s, %s)
    """

    values = (site_name, site_url, site_username_email, site_password, date_created)
    cursor.execute(query, values)

    passdb.commit()
    cursor.close()
    passdb.close()


# Option 1 - Check Saved Logins
def get_data(username):
    # Connect to db
    cursor, passdb = initiate_db_connection(username)

    try:
        # ------Prints User DB Table-----
        print_table_now(cursor, username)

        # ------Gets Query Data --------
        # Execute the SQL statement to retrieve all rows from the table
        cursor.execute(f"SELECT * FROM {username}_Table")
        # Fetch the results
        results = cursor.fetchall()
        cursor.close()
        # print(results)
        return results
    # Returns False if no DB for the user
    except mysql.connector.Error as error:
        print(error)
        return False


def print_table_now(cursor, username):
    # Execute the SQL statement to show the list of tables
    cursor.execute("SHOW TABLES")

    # Fetch the results
    tables = cursor.fetchall()
    table_names = [table[0] for table in tables]

    username_table = f"{username}_Table"
    if username_table is not None and username_table in table_names:
        # Execute the SQL statement to select all rows from the table
        cursor.execute(f"SELECT * FROM {username_table}")

        # Fetch the results
        results = cursor.fetchall()

        # Create a rich Table
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("ID", style="dim", width=4)
        table.add_column("Site Name")
        table.add_column("Site Url")
        table.add_column("Username/Email")
        table.add_column("Password")
        table.add_column("Date & Time Created")

        # Add rows to the table
        for row in results:
            table.add_row(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]))

        # Print the table to the console
        console.print(table)

        # time.sleep(4)

# Main Funtion
def pass_manager_main(username):
    cursor, passdb = initiate_db_connection(username)
    
    print("""
    [1] -[yellow] Check Saved Login[/yellow]
    [2] -[yellow] Add New Login[/yellow]
    [3] -[yellow] Delete an entry[/yellow]
    [4] -[yellow] Delete all Database[/yellow]
    """)
    user_choice = input("[green]Enter your choice ")
    
    if user_choice == "1":
        results = get_data(username)

        if results:
            print("---------- Get Decrypted password -----------")
            print("Enter B to go back")
            get_id_site = int(input("Enter the ID of the site: ")) - 1

            if 0 <= get_id_site < len(results):
                password = results[get_id_site][4]
                print("Your Password is:", password)
            else:
                print("Invalid site ID")
    elif user_choice == "2":
        add_data(username)
    elif user_choice == "3":
        delete_id(id)
    elif user_choice == "4":
        cursor.execute(f"DROP DATABASE {username}_Database")
        print(f"Successfully deleted database '{username}_Database'")
    else:
        print("[red] Invalid Option")
    pass

if __name__ == "__main__":
    try:
        os.system("clear||cls")
        usernames = input("\n[red] Enter your username ")
        pass_manager_main(usernames)
    except KeyboardInterrupt:
        exit()
