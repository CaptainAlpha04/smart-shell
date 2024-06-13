import os

# ? Curl Weather Command

def weather(args):
    # Check if only one argument is provided
    try:
        if len(args) > 0:
            if len(args) == 1: 
                location = args[0]
            else:
                # If multiple arguments are provided, concatenate them with '+'
                location = ""
                for i in range(len(args)):
                    location = location + "+" + args[i]

            # Using CURL command to get the weather data

            os.system(f"curl https://wttr.in/{location}")
            print('\033[33mSpecial Thanks to wttr.in for the weather data!\033[0m')
        else:
            print("Usage: weather [location]")
    except: 
        print("Invalid Arguments for command 'weather'. Please provide a valid location")
        print("Usage: weather [location]")

# ? Curl IP address finder
def get_ip():
    try:
        print("Your IPV6 Address is: \033[32m")
        os.system("curl ifconfig.me")
        print('\033[0m\nSpecial Thanks to ifconfig.me for the IP data!')
    except:
        print("Invalid syntax for command 'ip?'! Please provide a valid syntax.")
        print("Usage: ip?")

# ? Curl Dictionary Command
def dict(args):
    try:
        # Check if only one argument is provided
        if len(args) == 1: 
            word = args[0]
        else:
            # If multiple arguments are provided, concatenate them with '+'
            word = ""
            for i in range(len(args)):
                word = word + "+" + args[i]

        # Using CURL command to get the dictionary data
        os.system(f"curl dict://dict.org/d:{word}")
        print('\033[33mSpecial Thanks to dict.org for the dictionary data!\033[0m')
    except:
        print("Invalid Arguments for command 'define?'! Please provide valid arguments.")
        print("Usage: dict [word]")

# ? Curl QR Code Generator
def qrcode(args):
    try:
        if len(args) == 0:
            print("Usage: qr? [text]")
        else:
            # Using CURL command to get the QR Code
            os.system(f"curl qrenco.de/{args[0]}")
            print('\033[33mSpecial Thanks to qrenco.de for the QR Code!\033[0m')
    except: 
        print("Invalid Arguments for command 'qr?'! Please provide valid arguments.")
        print("Usage: qr? [text]")
