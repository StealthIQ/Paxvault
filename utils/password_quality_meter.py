from rich.console import Console
from rich.progress import Progress
from rich.table import Table
from rich import print
import time
import os
import getpass
import sys
import pwnedpasswords
from password_strength import PasswordStats

# Function to check the password strength - x5 Rules
def check_password_strength(password):
    # Starting Score
    score = 0
    length = len(password)
    progress = Progress()
    # Table Tittle etc...
    rule_table = Table(show_header=True, header_style="bold magenta")
    rule_table.add_column("Rule")
    rule_table.add_column("Points", justify="right")

    # Rule 1: Min 8 characters
    rule1_points = 15 if length >= 8 else 0
    rule_table.add_row("At least 8 characters", f"[green]{rule1_points}[/green]")
    score += rule1_points

    # Rule 2: Contains both upper and lowercase characters
    has_upper = any(c.isupper() for c in password) # ittrates over each character in password c and returns true if any()
    has_lower = any(c.islower() for c in password) # " "
    rule2_points = 15 if has_upper and has_lower else 0
    rule_table.add_row("Contains both uppercase and lowercase characters", f"[green]{rule2_points}[/green]")
    score += rule2_points

    # Rule 3: Contains numbers
    has_number = any(c.isdigit() for c in password)
    rule3_points = 15 if has_number else 0
    rule_table.add_row("Contains numbers", f"[green]{rule3_points}[/green]")
    score += rule3_points

    # Rule 4: Contains symbols
    has_symbol = any(c.isalnum() == False for c in password)
    rule4_points = 15 if has_symbol else 0
    rule_table.add_row("Contains symbols", f"[green]{rule4_points}[/green]")
    score += rule4_points

    # Rule 5: Check if its a common password using pwnedpasswords lib
    common_passwords = pwnedpasswords.check(password, plain_text=True)
    rule5_points = 0 if bool(common_passwords) == True else 15
    rule_table.add_row("Not a common password", f"[green]{rule5_points}[/green]")
    score += rule5_points

    # Rule 6: Advanced Strength Score
    stats = PasswordStats(password)
    extensive_test_points = int((stats.strength()) * 100)/100*25
    rule_table.add_row("Advanced Strength Test", f"[green]{int(extensive_test_points)}[/green]")
    score += int(extensive_test_points)

    # Rule table
    console = Console()
    console.print("[bold magenta]\n 🔒Password Strength Checker \n[/bold magenta]")
    console.print(rule_table)

    # Progress bar
    task = progress.add_task("Scoring", total=100)
    for i in range(-1, int(score)):
        progress.advance(task, i)
        if i <= score:
            progress.start()
            time.sleep(0.01)
            progress.update(task, completed=i+1)
            # progress.stop()
            progress.refresh()
    progress.stop()

    return score

# Main function shit
def Passoword_Checker():
    try:
        password = getpass.getpass(prompt="\n Enter your password → ", stream=None)

        score = check_password_strength(password)
        print(f"\n[green] :beginner: Your password scored {score}/100 in [bold green]Basic Strength Test")
        stats = PasswordStats(password)
        extensive_test = (stats.strength()) * 100
        print(f"\n[red] :rocket: Your password scored {int(extensive_test)}/100 in [bold red]Advanced Strength Test\n")
        # xdf = print("\t[bold red]Enter any key to go back →[/bold red]") 
        input(("Enter any key to go back ..."))
            # exit()

    except KeyboardInterrupt:
        os.system("clear||cls")
        exit()

if __name__ == "__main__":
    Passoword_Checker()

