import os
from modules import basic_cmd as bc
from modules import curl_cmd as cc
from modules import utils as util

def startup():
    os.system('cls')
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
            if cmd == 'help':
                bc.help()
                
            elif cmd == 'cls': 
                startup()

            elif cmd == 'ls':
                bc.ls(args)

            elif cmd == 'cd':
                bc.cd(args)

            elif cmd == 'mkdir':
                bc.mkdir(args)

            elif cmd == 'mkfile':
                bc.mkfile(args)
                
            elif cmd == 'rm':
                bc.rm(args)

            elif cmd == 'cp':
                bc.cp(args)
            
            elif cmd == 'mv':
                bc.mv(args)

            elif cmd == 'ren':
                bc.ren(args)

            elif cmd == 'printc':
                bc.printc(args)
            
            elif cmd == 'exit':
                print("Thank You for trying out the Smart Shell!")
                break
                
            # ? Specialized Commands
            elif cmd == 'ip?':
                cc.get_ip()

            elif cmd == 'randnum':
                util.randnum(args)

            elif cmd == 'screenfetch':
                util.screenfetch(args)

            # * Curl Related Commands

            elif cmd == 'weather?':
                cc.weather(args)

            elif cmd == 'define?':
                cc.dict(args)

            elif cmd == 'qrcode?':
                cc.qrcode(args)
            
            elif cmd == 'randnum':
                util.randnum(args)

            else: 
                print(f"Command '{cmd}' not found. Type 'help' for a list of commands.")
            

# *TODO: Fix the except block to handle the KeyboardInterrupt exception
    except KeyboardInterrupt:
        print("Exiting Smart Shell")
startup()