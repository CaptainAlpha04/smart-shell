
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
    {"command": "sysinfo", "description": "Print system information"}
]

# Help Function to display the list of commands
def help():
    print("List of commands:")
    for command in commands:
        print(f"{command['command']}:\t\t\t{command['description']}")
