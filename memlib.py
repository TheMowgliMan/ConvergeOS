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

    # Adds another item to memory, and returns the location. Return format: returns location
    def append(self, data):
        if len(self.memory) > self.max_size:
            raise MemoryError("Attempted to append an item with memory full. Length set: " + str(self.max_size))

            # Just in case!
            return None
        else:
            self.memory.append(data)
            return len(self.memory) - 1

    # Fetches an item from memory. Return format: None if error or undefined location, otherwise the data at the memory location
    def read(self, location):
        if location > self.max_size:
            raise ValueError("Attempted to read a location beyond memory range.")

            # Just in case?
            return None
        elif location > len(self.memory) - 1 and self.debug_on:
            warnings.warn("Attempted to access a non-defined memory location.")
            return None
        else:
            return self.memory[location]