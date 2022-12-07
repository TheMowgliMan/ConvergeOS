# convergeos.py
# The main file for the ConvergeOS project.
# Main author: @TheMowgliMan
# Contributors: 
# This is the kernal for the OS. It runs all the core code; frequently used functions and functions + classes that may be used
# in other files or that are highly modular should be their own modules in a separate file. This file should not exceed 1000 lines unless additional
# functionality cannot be added into other files.

import syslib as sys
import memlib
import cmdlib

debug = True

print("ConvergeOS Pre-alpha 0.0.1.33. Debug auto-on.")

sys.print_prio("Activating memlib...", debug)
memory = memlib.MemoryManager(maximum_size = 16384, debug = debug)

sys.print_prio("Entering CLI.", debug)

while True:
    inp = sys.split_command(input("?> "))
    command = inp[0]
    inputs = inp[1]

    cmdlib.process_command(command, inputs)