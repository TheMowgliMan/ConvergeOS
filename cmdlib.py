# cmdlib.py
# This file has the command functions.
# Author: @TheMowgliMan
# Other Contributors:


from syslib import reassemble
import warnings


# Prints a string or list to stdout; raises error if wrong type.
def echo(text):
    if isinstance(text, str):
        print(text)
    elif isinstance(text, list):
        print(reassemble(text))
    else:
        raise TypeError("Echo only takes a string or list!")

# Evaluates a single line of python
def evaluate(text):
    if isinstance(text, list):
        ret = eval(reassemble(text))
        print(ret)
    else:
        raise TypeError("Eval only takes a string or list!")

# Exits the OS
def exit_os(inputs):
    if inputs != []:
        print("Note: Exit uses no inputs.")

    warnings.warn("Note that Exit forcibly closes the OS! Any running programs in the background will be forcibly terminated.")

    print("Exiting...")

    exit()

def process_command(command, input):
    if command == "echo":
        echo(input)
    elif command == "eval":
        evaluate(input)
    elif command == "exit":
        exit_os(input)
    else:
        warnings.warn("Command " + command + " does not exist.")
