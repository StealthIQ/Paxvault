import os
import time
import mysql.connector
from rich.console import Console
from rich.table import Table
from rich import print
from rich.prompt import Prompt as input

console = Console()

# try:
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    auth_plugin='mysql_native_password'
    )

# variable cursor
cursor = mydb.cursor()
# except mysql.connector.Error as error:
    # print("Failed to connect to MySQL database: {}".format(error))

# Creating a database Passfx 
cursor.execute("CREATE DATABASE IF NOT EXISTS Passfx")

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="Passfx"
    )


cursor = mydb.cursor()

# Creating a table for the database Passfx
cursor.execute("""
CREATE TABLE IF NOT EXISTS Passfx_Users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    main_key VARCHAR(255) NOT NULL,
    email_hash VARCHAR(255) NOT NULL,    
    cipher_iv_email VARCHAR(255) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    cipher_iv_password VARCHAR(255) NOT NULL,
    date_time_created VARCHAR(255)
)
               """)

# Passfx User Function to add new usernames, pass etc.. into the table
def Passfx_Users_Add(username, main_key, email_hash, cipher_iv_email, password_hash, cipher_iv_password, date_time_created):
 
    # Connect to the database
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="Passfx"
    )

    cursor = mydb.cursor()

   # Insert the new user information into the master_users table
    query = """
    INSERT INTO Passfx_Users (username, main_key, email_hash, cipher_iv_email, password_hash, cipher_iv_password, date_time_created)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    values = (username, main_key, email_hash, cipher_iv_email, password_hash, cipher_iv_password, date_time_created)
    cursor.execute(query, values)

    mydb.commit()

    cursor.close()
    mydb.close()

def Passfx_login_verify(username):

    # Connect to the database
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="Passfx"
    )

    cursor = mydb.cursor()

    # Retrieve the user information from the Passfx_Users table
    query = """
    SELECT username, main_key, email_hash, cipher_iv_email, password_hash, cipher_iv_password, date_time_created    
    FROM Passfx_Users
    WHERE username = %s 
    """
    values = (username,)  # add comma here to create a tuple with one element  
    cursor.execute(query, values)
    result = cursor.fetchone()

    cursor.close()
    mydb.close()
    
    # print(result)
    return result

#--------------------------[sql_db_setting]----------------------------------
def sql_db_setting():

    cursor = mydb.cursor()

    # os.system('clear||cls')
    print("""[purple]
    [1] - Delete Database Passfx
    [2] - Delete Table Passfx_Users
    [3] - Show All Table
    [4] - Print All the result in the Table
[/purple]""")
    user_choice = input.ask("[red]    [!] Choose the right option[/red]")

    # Passfx_Users_Add("Logan", "gAAAAABkWpuSRm3gwN2JXKibqc7GUBvV8X45__0CPHg33WdNw7wgg34VtEcK9rl5rNPmMnekcrofdECNY_MM-dQN6MQRpWWwAA==", "b'nnzpfnNXzU8d2k_LhXqwU1wrLOKUyXE2GjDdD8F8-6Q='", "gAAAAABkWpuSYwogqYlkG48dCba6LDU-jxcaf7WS7Z9PnqajOkuteT2wgrVa8U6wACDCdBTptymjhp0NVWY3GcNWWbd145FEFg==", "10-05-2023 00:44:23")
    if user_choice == "1":
        # Execute the SQL statement to --------------[DELETE]------------- the database 
        cursor.execute("DROP DATABASE Passfx")
        print("Successfully deleted database 'Passfx'")
    elif user_choice == "2":
        # Execute the SQL statement to --------------[DELETE]------------- the table
        cursor.execute("DROP TABLE Passfx_Users")
        print("Successfully deleted Table 'Passfx_Users'")
    elif user_choice == "3":
        # Execute the SQL statement to show the list of tables
        cursor.execute("SHOW TABLES")
    
        # Fetch the results
        tables = cursor.fetchall()

        # Print the list of tables
        for table in tables:
          print(table[0])
    elif user_choice == "4":   
        # Execute the SQL statement to select all rows from the table
        cursor.execute("SELECT * FROM Passfx_Users")
        
        # Fetch the results
        results = cursor.fetchall()
        
        # # Print the results
        # for row in results:
        #     print(row)

        # Create a rich Table
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("ID", style="dim", width=4)
        table.add_column("Username")
        table.add_column("Main key")
        table.add_column("Email Hash")
        table.add_column("Email Cipher Hash")
        table.add_column("Password Hash")
        table.add_column("Password Cipher Hash")
        table.add_column("Date & Time Created ")
        
        # Add rows to the table
        for row in results:
            # table.add_row(str(row["ID"]), str(row["Username"]), str(row["Main key"]), str(row["Email Hash"]), str(row["E-Cipher Hash"]), str(row["Password Hash"]), str(row["P-Cipher Hash"]), str(row["D:T Created"]))
            table.add_row(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]))

        
        # Print the table to the console
        console.print(table)
    else:
        exit()
    
    # Commit the changes
    mydb.commit()
    
    # Close the cursor and database connections
    # cursor.close()
    # 
    # mydb.close()
    input.ask("")
   
if __name__ == "__main__":
    sql_db_setting()
