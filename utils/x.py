import mysql.connector
import time
from rich.table import Table
from rich import print as console

def initiate_db_connection(username):
    """Connect to the database and return a cursor"""
    passdb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database=f"{username}_Database"
    )
    return passdb.cursor(), passdb


def add_data(username):
    # Connect to the database
    cursor, passdb = initiate_db_connection(username)

    site_name = input("Enter the site name: ")
    site_url = input("Enter the site URL: ")
    site_username_email = input("Enter the username/email used for the site: ")
    site_password = input("Enter the password: ")
    date_created = input("Enter the date and time created: ")

    # Creating a table for the database
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
    VALUES (%s, %s, %s, %s, %s)
    """

    values = (site_name, site_url, site_username_email, site_password, date_created)
    cursor.execute(query, values)

    passdb.commit()
    cursor.close()
    passdb.close()


def get_data(username, print_table=False, get_query=False):
    # Connect to the database
    cursor, passdb = initiate_db_connection(username)

    if print_table:
        print_table_now(cursor, username)

    if get_query:
        # Execute the SQL statement to retrieve all rows from the table
        cursor.execute(f"SELECT * FROM {username}_Table")
        # Fetch the results
        results = cursor.fetchall()
        cursor.close()
        passdb.close()
        return results


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
        console(table)

        time.sleep(4)


# Main Function
def pass_manager_main(username):
    cursor, passdb = initiate_db_connection(username)
    # Creating a database for the password manager
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {username}_Database")

    print("""
    [1] -[yellow] Check Saved Login[/yellow]
    [2] -[yellow] Add New Login[/yellow]
    [3] -[yellow] Delete an entry[/yellow]
    [4] -[yellow] Delete all Database[/yellow]
    """)
    user_choice = input("[green]Enter your choice: ")

    if user_choice == "1":
        get_data(username, print_table=True)
        print("""---------- Get Decrypted password -----------
                                        Enter B to go back""")
        get_id_site = int(input("Enter the ID of the site: ")) - 1
        username_query_value = get_data(username, get_query=True)
        if get_id_site in username_query_value[0]:
            print("Your Password is:", username_query_value[get_id_site][4])


# Testing the code
username = input("Enter the username: ")
pass_manager_main(username)
