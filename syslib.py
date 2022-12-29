# syslib.py
# This file provides miscellanious utilities such as a priority print function.
# Author: @TheMowgliMan
# Other Contributors:

import os

# Prority print- I.e. prints only if debug is true
def print_prio(text, debug):
    if debug == True:
        print(text)

# Splits a command up as needed. Return format: ["command", ["input 1", "input 2"]]
def split_command(cmd):
    inp = cmd.split(" ")
    inputs = None
    command = inp[0]
    del inp[0]
    inputs = inp

    # print([command, inputs])

    return [command, inputs]

# Takes a string and replaces the default set of characters
def filter(string):
    # Takes NLCR and replaces it with a newline
    out = str(string).replace(" nlcr ", "\n")
    out = out.replace(" nlcr", "\n")
    out = out.replace("nlcr ", "\n")
    out = out.replace("nlcr", "\n")
    out = out.replace(" NLCR ", "\n")
    out = out.replace(" NLCR", "\n")
    out = out.replace("NLCR ", "\n")
    out = out.replace("NLCR", "\n")

    return out

# Takes a list of strings and reassembles them into a string
def reassemble(list, sep = " ", filter_str = False):
    out = ""
    for i in list:
        if i == "nlcr":
            out = out + "\n" + sep
        else:
            out = out + i + sep

    if filter_str:
        return filter(out)
    else:
        return out

# Creates the userspace filesystem
def install_filesystem():
    os.mkdir("/userspace")
    os.mkdir("/userspace/system")
    os.mkdir("/userspace/system/log")
    os.mkdir("userspace/system/apps")
    os.mkdir("userspace/user")
    os.mkdir("userspace/user/documents")
    os.mkdir("userspace/user/desktop")
    os.mkdir("userspace/user/images")
    os.mkdir("userspace/user/appdata")
