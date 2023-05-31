import os
import random
import fade


def banner_art():
    os.system("clear||cls")
    ART = ("""
         ███████████       |
       ████       ████     | ██████╗  █████╗ ██╗  ██╗██╗   ██╗ █████╗ ██╗   ██╗██╗  ████████╗
      ███           ███    | ██╔══██╗██╔══██╗╚██╗██╔╝██║   ██║██╔══██╗██║   ██║██║  ╚══██╔══╝
      ███           ███    | ██████╔╝███████║ ╚███╔╝ ██║   ██║███████║██║   ██║██║     ██║   
      ██████████████████   | ██╔═══╝ ██╔══██║ ██╔██╗ ╚██╗ ██╔╝██╔══██║██║   ██║██║     ██║   
    █████████████████████  | ██║     ██║  ██║██╔╝ ██╗ ╚████╔╝ ██║  ██║╚██████╔╝███████╗██║   
    ██████████████▓▒▒P▒▒▓  | ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝   
    ██████████████▓██████  |                                  [Next Gen CLI-Password Manager]
    ██████████████▓▒▒X▒▒▓  | [DEVELOPERS ↙                    [AES-256 Encryption]
    ██████████████▓██████  | [Stealthiq]            
    ████████████████████▓  | 
""")

    #Banner Art - Using fade module for gradient
    fade_gradients = [fade.blackwhite(ART), fade.purplepink(ART), fade.greenblue(ART), fade.water(ART), fade.fire(ART), fade.pinkred(ART), fade.purpleblue(ART), fade.brazil(ART)]
    randomx = (random.choice(fade_gradients))

    faded_text = randomx
    print(faded_text)

if __name__ == "__main__":
    banner()


