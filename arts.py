import os
import fade
import time
from rich.console import Console
from rich import print as print
from rich.prompt import Prompt
import random
from utils.just_banner import banner_art

input = Prompt.ask

#Up time module
start_time = time.time()

Main_modules = (f"[cyan]    //////////////////////////////////[[red] COMMANDS HERE [cyan]]//////////////////////////////////\n[yellow]")

def banner():

    banner_art()

    Main_modules = (f"[cyan]    //////////////////////////////////[[red] COMMANDS HERE [cyan]]//////////////////////////////////\n[yellow]")
    print(Main_modules)


def Start_modules():
    # Uptime module
    global uptime_x
    elapsed_time = time.time() - start_time
    uptime_x = ("{:.2f} SEC".format(elapsed_time))

    start_menu = f"""    [green][[white]1[green]] LOG IN                                                                        
    [green][[white]2[green]] REGISTER                                   [red][[white]VERSION[red]] 1.0 (BETA)                          
    [green][[white]3[green]] SETTINGS                                   [red][[white]UP-TIME[red]] {uptime_x}               
    [green][[white]4[green]] GITHUB                                     [red][[white]PX-QUIT[red]] Q / CTRL +C                 
"""
    # print(Main_modules)
    print(start_menu)
    # time.sleep(5)

#Main Modules
def Main_modules():

    main_menu = f"""    [green][[white]1[green]] PASSWORD MANAGER                                                                        
    [green][[white]2[green]] PASSWORD GENERATOR                                  [red][[white]VERSION[red]] 1.0 (BETA)                          
    [green][[white]3[green]] PASSPHRASE GENERATOR                                [red][[white]GO-BACK[red]] B to BACK
    [green][[white]4[green]] PASSWORD QUALITY METER                              [red][[white]PX-QUIT[red]] Q / CTRL +C                 
"""
    # print(Main_modules)
    print(main_menu)
    # time.sleep(5)
