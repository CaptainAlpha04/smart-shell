import os
import datetime
import random

#? Username command
def whoami():
    try:
        print(f"Current User: {os.getlogin()}")
    except:
        print("An error occurred while fetching the current user.")

#? date and time command
def dt(args):
    try:
        if len(args) == 0:
            print(f"Current Date: {datetime.datetime.now().date()} Current Time: {datetime.datetime.now().time()}")
        elif args[0] == 'date':
            print(f"Current Date: {datetime.datetime.now().date()}")
        elif args[0] == 'time':
            print(f"Current Time: {datetime.datetime.now().time()}")
        else:
            print("Invalid Arguments for command 'dt'.")
            print("Usage: dt or dt [date] or dt [time]")
    except:
        print("Invalid Arguments for command 'dt'.")
        print("Usage: dt")

def sysinfo():
    try:
        if os.name == 'nt':
            os.system("systeminfo")
        else:
            os.system("neofetch")
    except:
        print("An error occurred while fetching system information.")

# ? Random Number Generator

def randnum(args):
    try:
        if len(args) == 0:
            print(f"{random.randint(0, 100)}")
        elif len(args) == 1:
                num = int(args[0])
                print(f"{random.randint(0, num)}")
        elif len(args) == 2:
                num1 = int(args[0])
                num2 = int(args[1])
                print(f"{random.randint(num1, num2)}")
    except:
        print("Invalid Arguments. Please provide a valid range.")
        print("Usage: randnum or randnum [limit] or randnum [start] [end]")

# ? screenfetch command to display system information and logo
def screenfetch(args):
    try:
        if len(args) == 0:
            if os.name == 'nt':
                print(f"Operating System: {os.name}")
            else:
                os.system("screenfetch")
        else:
            print("Invalid Arguments for command 'screenfetch'.")
            print("Usage: screenfetch")
    except:
        print("Invalid Arguments for command 'screenfetch'.")
        print("Usage: screenfetch")
