# syslib.py
# This file provides miscellanious utilities such as a priority print function.
# Author: @TheMowgliMan
# Other Contributors:

# Prority print- I.e. prints only if debug is true
def print_prio(text, debug):
    if debug == True:
        print(text)

# Splits a command up as needed. Return format: ["command", ["input 1", "input 2"]]
def split_command(cmd):
    inp = cmd.split(" ")
    inputs = ""
    command = inp[0]
    del inp[0]
    inputs = inp

    return [command, inputs]