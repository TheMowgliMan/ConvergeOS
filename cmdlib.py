# cmdlib.py
# This file has the command functions.
# Author: @TheMowgliMan
# Other Contributors:


# Prints a string or list to stdout; raises error if wrong type.
def echo(text):
    if isinstance(text, str):
        print(text)
    elif isinstance(text, list):
        out = ""
        for i in text:
            out = out + i + " "

        print(out)
    else:
        raise TypeError("Echo only takes a string or list!")

def process_command(command, input):
    if command == "echo":
        echo(input)
