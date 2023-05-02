"""
Author: new92
Github: @new92
"""

from random import choice
from Entrance import main


def Jack():
    def JP() -> str:
        return """
        ██╗██╗██╗░░░░░██╗░█████╗░░█████╗░██╗░░██╗██████╗░░█████╗░████████╗██╗██╗██╗
        ██║██║██║░░░░░██║██╔══██╗██╔══██╗██║░██╔╝██╔══██╗██╔══██╗╚══██╔══╝██║██║██║
        ██║██║██║░░░░░██║███████║██║░░╚═╝█████═╝░██████╔╝██║░░██║░░░██║░░░██║██║██║
        ╚═╝╚═╝╚═╝██╗░░██║██╔══██║██║░░██╗██╔═██╗░██╔═══╝░██║░░██║░░░██║░░░╚═╝╚═╝╚═╝
        ██╗██╗██╗╚█████╔╝██║░░██║╚█████╔╝██║░╚██╗██║░░░░░╚█████╔╝░░░██║░░░██╗██╗██╗
        ╚═╝╚═╝╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░░░░░╚════╝░░░░╚═╝░░░╚═╝╚═╝╚═╝
        """
    def JackPot(pot, val):
        return [choice(pot) for i in range(3)] in val
    def convert(chips):
        return chips * 1000
    cost = 2
    chips = main()
    icons = ["🍉","🍒","🍌"]
    jackpot = [["🍉","🍉","🍉"],["🍒","🍒","🍒"],["🍌","🍌","🍌"]]
    end=str(input("[?] Stop ? [Y/N] >> "))
    while chips > 0 and end in ['N','n']:
        if JackPot(icons, jackpot):
            print(JP())
            chips += 10
        else:
            chips -= cost
        end=str(input("[?] Stop ? [Y/N] >> "))
    return False if chips == 0 else convert(chips)