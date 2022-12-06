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
            data = str(line).split("|")
            for command in data:
                cmdinp = command.split("-")

                if cmdinp[0] == "APPEND":
                    del cmdinp[0]
                    out = out + syslib.reassemble(cmdinp)
                if cmdinp[0] == "FILE":
                    del cmdinp[0]
                    out = out + self.FILE(cmdinp)

        return out

    def FILE(self, inputs):
        if len(inputs) == 1:
            try:
                file_handler = open(inputs[0], 'r')
                ret_data = file_handler.read()
                file_handler.close()

                return ret_data
            except IOError:
                print("File '" + inputs[0] + "' does not exist.")
        else:
            print("Incorrect number of arguments for FILE.")

# Testing code
if __name__ == "__main__":
    cmdproc = CmdprocInterpreter()
    print(cmdproc.interpret("FILE-syslib.py|APPEND-NLCRline one NLCR line two-smth else"))