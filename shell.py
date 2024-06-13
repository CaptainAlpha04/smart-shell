import os
from modules import basic_cmd as bc
from modules import curl_cmd as cc
from modules import utils as util
from modules import ai_tools as ai

def startup():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    screen = """\033[36m
                ███████╗███╗   ███╗ █████╗ ██████╗ ████████╗    ███████╗██╗  ██╗███████╗██╗     ██╗     
                ██╔════╝████╗ ████║██╔══██╗██╔══██╗╚══██╔══╝    ██╔════╝██║  ██║██╔════╝██║     ██║     
                ███████╗██╔████╔██║███████║██████╔╝   ██║       ███████╗███████║█████╗  ██║     ██║     
                ╚════██║██║╚██╔╝██║██╔══██║██╔══██╗   ██║       ╚════██║██╔══██║██╔══╝  ██║     ██║     
                ███████║██║ ╚═╝ ██║██║  ██║██║  ██║   ██║       ███████║██║  ██║███████╗███████╗███████╗
                ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝
                                                                                        \033[0m"""
    print(screen)
    print("Welcome to the Smart Shell! Version 1.0.0")
    print("Type 'help' for a list of commands. Type exit to quit the shell.")
    main_process()

def main_process():
    try:
        while True:
            cmd_input = input(f'\033[36m\nsmsh#\033[33m{"Home" if os.getcwd().endswith("Home") else os.getcwd()}>\033[0m ')

            if not cmd_input:
                continue

            sh_cmd = cmd_input.split()

            cmd = sh_cmd[0].lower()
            args = sh_cmd[1:]

######### Command Execution ############
        # ? Standard Commands
            if cmd == 'help': # Display the list of commands
                bc.help()
                
            elif cmd == 'cls': # Clear the terminal screen
                startup()

            elif cmd == 'ls': # List all files in the current directory
                bc.ls(args)

            elif cmd == 'pwd': # Print the current working directory
                bc.pwd()

            elif cmd == 'cd':   # Change the current working directory
                bc.cd(args)

            elif cmd == 'mkdir': # Create a new directory
                bc.mkdir(args)

            elif cmd == 'mkfile': # Create a new file
                bc.mkfile(args)
                
            elif cmd == 'rm': # Remove a file or directory
                bc.rm(args)

            elif cmd == 'cp': # Copy a file or directory
                bc.cp(args)
            
            elif cmd == 'mv': # Move a file or directory
                bc.mv(args)

            elif cmd == 'ren': # Rename a file or directory
                bc.ren(args)

            elif cmd == 'printf': # Print the content of a file to the terminal
                bc.printf(args)

            elif cmd == 'prints': # Print a string to the terminal
                bc.prints(args)
            
            elif cmd == 'exit': # Exit the Smart Shell
                print("Thank You for trying out the Smart Shell!")
                return
                
            # ? Specialized Commands
            elif cmd == 'ip?': # Get the IP address of the system
                cc.get_ip()

            elif cmd == 'screenfetch': # Display system information and logo
                util.screenfetch(args)

            elif cmd == 'dt': # Print the current date and time
                util.dt(args)

            elif cmd == 'whoami': # Print the current user
                util.whoami()
            # * Curl Related Commands

            elif cmd == 'weather?': # Get the weather data
                cc.weather(args)

            elif cmd == 'define?': # Get the dictionary data
                cc.dict(args)

            elif cmd == 'qrcode?': # Generate a QR Code
                cc.qrcode(args)
            
            elif cmd == 'randnum': # Generate a random number
                util.randnum(args)

            #? Chat with AI capabilities
            elif cmd == '@neo': # Chat with the AI
                ai.neo(args)
            else: # If the command is not found
                print(f"Command '{cmd}' not found. Type 'help' for a list of commands.")
            

# *TODO: Fix the except block to handle the KeyboardInterrupt exception
    except KeyboardInterrupt:
        print("Exiting Smart Shell")

startup()
