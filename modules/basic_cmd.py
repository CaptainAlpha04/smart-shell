import os
# Commands list for the Smart Shell help
commands = [
    {"command": "help", "description": "List of commands"},
    {"command": "exit", "description": "Exit the Smart Shell"},
    {"command": "ls", "description": "List all files in the current directory"},
    {"command": "pwd", "description": "Print the current working directory"},
    {"command": "cd", "description": "Change the current working directory"},
    {"command": "mkdir", "description": "Create a new directory"},
    {"command": "rm", "description": "Remove a file or directory"},
    {"command": "cp", "description": "Copy a file or directory"},
    {"command": "mv", "description": "Move a file or directory"},
    {"command": "cat", "description": "Display the contents of a file"},
    {"command": "touch", "description": "Create a new file"},
    {"command": "print", "description": "Print a string to the terminal"},
    {"command": "cls", "description": "Clear the terminal screen"},
    {"command": "dt", "description": "Print the current date and time"},
    {"command": "whoami", "description": "Print the current user"},
    {"command": "sysinfo", "description": "Print system information"},
    {"command": "randnum", "description": "Generate a random number"}
]

#? Help Function to display the list of commands
def help():
    print("List of commands:")
    for command in commands:
        print(f"{command['command']}:\t\t\t{command['description']}")

#? List all files in the current directory
def ls(args):
    dir_content = ""
    try:
        if len(args) == 0:
            content = os.listdir(os.getcwd())
            for file in content:
                if os.path.isdir(file):
                    dir_content += "\033[32m" + file + "\033[0m" + "\t\t"
                else: 
                    dir_content += "\033[34m" + file + "\033[0m" + "\t\t"
            print(dir_content)
        elif len(args) == 1:
            content = os.listdir(args[0])
            for file in content:
                if os.path.isdir(file):
                    dir_content += "\033[32m" + file + "\033[0m" + "\t\t"
                else: 
                    dir_content += "\033[34m" + file + "\033[0m" + "\t\t"
            print(dir_content)
        else: 
            print("Incorrect Syntax! Usage: ls or ls [directory]")
    except:
        print("Invalid Arguments for command 'ls'. Please provide a valid syntax.")
        print("Usage: ls or ls [directory]")

#? Create a new directory
def mkdir(args):
    try:
        if len(args) == 0:
            print("Usage: mkdir [directory]")
        else:
            directory = args[0]
            if directory.startswith('"') and directory.endswith('"'):
                directory = directory[1:-1]
            os.mkdir(directory)
    except:
        print("Invalid Arguments for command 'mkdir'. Please provide a valid directory name.")
        print("Usage: mkdir [directory]")

#? Create a new file
def mkfile(args):
    try:
        if len(args) == 0:
            print("Usage: mkfile [file]")
        else:
            file_name = args[0]
            if file_name.startswith('"') and file_name.endswith('"'):
                file_name = file_name[1:-1]
            with open(file_name, 'w') as file:
                pass
            print(f"File {file_name} created successfully!")
    except:
        print("Invalid Arguments for command 'mkfile'. Please provide a valid file name.")
        print("Usage: mkfile [file]")

#? Remove a file or directory
def rm(args):
    try:
        if len(args) == 0:
            print("Usage: rm [file/directory]")
        else:
            if os.name == 'nt':
                os.system(f"del {args[0]}")
            else:
                os.system(f"rm -r {args[0]}")
    except:
        print("Invalid Arguments for command 'rm'. Please provide a valid file/directory name.")
        print("Usage: rm [file/directory]")

#? Copy a file or directory
def cp(args):
    try:
        if len(args) == 0:
            print("Usage: cp [source] [destination]")
        elif len(args) == 1:
            print("Usage: cp [source] [destination]")
        else:
            if os.name == 'nt':
                os.system(f"copy {args[0]} {args[1]}")
            else:
                os.system(f"cp {args[0]} {args[1]}")
    except:
        print("Invalid Arguments for command 'cp'. Please provide a valid source and destination.")
        print("Usage: cp [source] [destination]")

#? Move a file or directory
def mv(args):
    try:
        if len(args) == 0:
            print("Usage: mv [source] [destination]")
        elif len(args) == 1:
            print("Usage: mv [source] [destination]")
        else:
            if os.name == 'nt':
                os.system(f"move {args[0]} {args[1]}")
            else:
                os.system(f"mv {args[0]} {args[1]}")
    except:
        print("Invalid Arguments for command 'mv'. Please provide a valid source and destination.")
        print("Usage: mv [source] [destination]")

#? Display the contents of a file
def printc(args):
    try:
        if len(args) == 0:
            print("Usage: cat [file]")
        else:
            if os.name == 'nt':
                os.system(f"type {args[0]}")
            else:
                os.system(f"cat {args[0]}")
    except:
        print("Invalid Arguments for command 'printc'. Please provide a valid file name.")
        print("Usage: printc [file]")

#? Change the directory
def cd(args):
    try:
        if len(args) == 0:
            print("Usage: cd [directory]")
        elif len(args) == 1 and (args[0] == ".." or args[0] == "../" or args[0] == "/"):
            os.chdir("..")
        elif len(args) == 1 and args[0] == "~":
            os.chdir(os.path.expanduser("~"))
        else:
            os.chdir(args[0])
    except:
        print("Invalid Arguments for command 'cd'. Please provide a valid directory name.")
        print("Usage: cd [directory]")

#? Rename a file or directory
def ren(args):
    try:
        if len(args) != 2:
            print("Usage: ren [old_name] [new_name]")
        else:
            if os.path.exists(args[0]):
                os.rename(args[0], args[1])
            else:
                print(f"{args[0]} does not exist!")
    except:
        print("Invalid Arguments for command 'ren'. Please provide a valid old and new name.")
        print("Usage: ren [old_name] [new_name]")

