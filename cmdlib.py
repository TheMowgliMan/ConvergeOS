# cmdlib.py
# This file has the command functions.
# Author: @TheMowgliMan
# Other Contributors:


from syslib import reassemble


# Prints a string or list to stdout; raises error if wrong type.
def echo(text):
    if isinstance(text, str):
        print(text)
    elif isinstance(text, list):
        print(reassemble(text))
    else:
        raise TypeError("Echo only takes a string or list!")

def process_command(command, input):
    if command == "echo":
        echo(input)
