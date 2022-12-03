# cmdlib.py
# This file has the command functions.
# Author: @TheMowgliMan
# Other Contributors:

def echo(text):
    if isinstance(text, str):
        print(text)
    elif isinstance(text, list):
        out = ""
        for i in text:
            out = out + i + " "

        print(out)
def process_command(command, input):
    if command == "echo":
        echo(input)
