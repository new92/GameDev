"""
Author: new92
Github: @new92
"""
from time import sleep
def logo() -> str:
    return """
    ░█████╗░░█████╗░░██████╗██╗███╗░░██╗░█████╗░
    ██╔══██╗██╔══██╗██╔════╝██║████╗░██║██╔══██╗
    ██║░░╚═╝███████║╚█████╗░██║██╔██╗██║██║░░██║
    ██║░░██╗██╔══██║░╚═══██╗██║██║╚████║██║░░██║
    ╚█████╔╝██║░░██║██████╔╝██║██║░╚███║╚█████╔╝
    ░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝╚═╝░░╚══╝░╚════╝░
    """

def main():
    print(logo())
    name=str(input("[::] Please enter your name: "))
    while name == None:
        name=str(input("[::] Please enter again your name: "))
    money=int(input("[::] Please enter the amount of money you want to gamble: "))
    while money < 1000:
        print("[!] Not enough money to gamble !")
        sleep(2)
        money=int(input("[::] Please enter again the amount of money you want to gamble: "))
    return int(money / 1000)