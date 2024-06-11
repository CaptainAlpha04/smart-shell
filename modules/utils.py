import os
import math
import random

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