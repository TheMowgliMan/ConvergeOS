# memlib.py
# This file provides utilities relating to memory storage for ConvergeOS.
# Author: @TheMowgliMan
# Other Contributors:


from syslib import print_prio
import warnings


class MemoryManager:
    def __init__(self, maximum_size = 16384, debug = False):
        print_prio("Memory manager initializing...", debug)

        self.max_size = maximum_size
        self.debug_on = debug
        self.memory = []

        print_prio("Memory manager initialization complete.", self.debug_on)

    # Adds another item to memory, and returns the location.
    def append(self, data):
        if len(self.memory) > self.max_size:
            raise MemoryError("Attempted to append an item with memory full. Length set: " + str(self.max_size))

            # Just in case!
            return -1
        else:
            self.memory.append(data)
            return len(self.memory) - 1

    # Fetches an item from memory
    def read(self, location):
        if location > self.max_size:
            raise ValueError("Attempted to read a location beyond memory range.")

            # Just in case?
            return -1
        elif location > len(self.memory) - 1 and self.debug_on:
            warnings.warn("Attempted to access a non-defined memory location.")
            return -1
        else:
            return self.memory[location]