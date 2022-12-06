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
        out = ""
        for line in string.split("\n"):
            data = str(line).split(" ")
            for command in data:
                cmdinp = command.split("-")

                if cmdinp[0] == "APPEND":
                    del cmdinp[0]
                    out = out + syslib.reassemble(cmdinp)

        return out

# Testing code
if __name__ == "__main__":
    cmdproc = CmdprocInterpreter()
    print(cmdproc.interpret("FILE-syslib.py APPEND-nlcr"))