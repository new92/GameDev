"""
Author: new92
Github: @new92

A (silly) game made with Python
"""
from mod import Jack
from time import sleep

def main():
    res = Jack()
    if type(res) == bool:
        print("[!] No more chips !")
        sleep(2)
        print("[+] Exiting Casino...")
        exit(0)
    else:
        print(f"[::] Claim your earnings: {res}$")
        sleep(2)
        exit(0)

if __name__ == '__main__':
    main()
