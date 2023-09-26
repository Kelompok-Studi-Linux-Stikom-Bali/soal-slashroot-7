import sys

blacklist = (
    "eval",
    "exec",
    "import",
    "open",
    "os",
    "read",
    "system",
    "write",
    ";",
    "+",
    "ord",
    "chr",
    "base",
    "flag",
    "replace",
    " ",
    "decode",
    "join"
)

print(" ██████╗██╗      █████╗  ██████╗██╗  ██╗██████╗  █████╗  █████╗ ████████╗  ███████╗    █████╗ ")
print("██╔════╝██║     ██╔══██╗██╔════╝██║  ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝  ╚════██║   ██╔══██╗")
print("╚█████╗ ██║     ███████║╚█████╗ ███████║██████╔╝██║  ██║██║  ██║   ██║         ██╔╝   ██║  ██║")
print(" ╚═══██╗██║     ██╔══██║ ╚═══██╗██╔══██║██╔══██╗██║  ██║██║  ██║   ██║        ██╔╝    ██║  ██║")
print("██████╔╝███████╗██║  ██║██████╔╝██║  ██║██║  ██║╚█████╔╝╚█████╔╝   ██║       ██╔╝  ██╗╚█████╔╝")
print("╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚════╝  ╚════╝    ╚═╝       ╚═╝   ╚═╝ ╚════╝ ")


while True:
    user_input = input("Enter your command: ")

    if any(keyword in user_input.lower() for keyword in blacklist):
        print("not not!")
        sys.exit()
    else:
        try:
            exec(user_input)
        except:
            print("Your input sucks :(")
