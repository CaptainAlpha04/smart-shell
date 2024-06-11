import os

# ? Curl Weather Command
def weather(args):
    # Check if only one argument is provided
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

# ? Curl IP address finder
def get_ip():
    print("Your IPV6 Address is: \033[32m")
    os.system("curl ifconfig.me")
    print('\033[0m\nSpecial Thanks to ifconfig.me for the IP data!')

# ? Curl Dictionary Command
def dict(args):
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

# ? Curl QR Code Generator
def qrcode(args):

    # Using CURL command to get the QR Code
    os.system(f"curl qrenco.de/{args[0]}")
    print('\033[33mSpecial Thanks to qrenco.de for the QR Code!\033[0m')
