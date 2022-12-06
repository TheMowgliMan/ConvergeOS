# cmdproc.py
# Allows a programming language-like amount of processing to terminal commands that support it.
# Main author: @TheMowgliMan
# Other contributors: 

import syslib

# This class allows interpretation of cmdproc commands.
class CmdprocInterpreter:
    def __init__(self):
        pass

    def interpret(self, string):
        print(string)

# Testing code
if __name__ == "__main__":
    cmdproc = CmdprocInterpreter()
    print(cmdproc.interpret("FILE-syslib.py APPEND-nlcr"))