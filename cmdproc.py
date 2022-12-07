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

            command_iter = 0
            for command in data:
                cmdinp = command.split("-")

                if cmdinp[0] == "APPEND":
                    del cmdinp[0]
                    out = out + syslib.reassemble(cmdinp, filter_str=True)
                elif cmdinp[0] == "FILE":
                    del cmdinp[0]

                    if command_iter > 0:
                        if data[command_iter - 1].split("-")[0] == "APPEND" and len(data[command_iter - 1].split("-")) == 0:
                            out = out + self.FILE(cmdinp)
                        else:
                            out = self.FILE(cmdinp)
                    else:
                        out = self.FILE(cmdinp)
                elif cmdinp[0] == "HELP":
                    del cmdinp[0]

                    if command_iter > 0:
                        if data[command_iter - 1].split("-")[0] == "APPEND" and len(data[command_iter - 1].split("-")) == 0:
                            out = out + self.HELP(cmdinp)
                        else:
                            out = self.HELP(cmdinp)
                    else:
                        out = self.HELP(cmdinp)


                command_iter += 1

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

    def HELP(self, inputs):
        if len(inputs) == 0:
            return "All Commands:\nAPPEND\nFILE\nHELP"
        else:
            if input[0] == "APPEND":
                return "APPEND-ar1-arg2: Appends each argument (separated by a space) to the output of the cmdproc set. Has special behavior for other commands."
            elif input[0] == "FILE":
                return "FILE-filename: Sets the output to the data in the chosen file. If preceded by an APPEND command with no arguments, appends it instead."
            elif input[0] == "HELP":
                return "HELP-command(optional). Sets the output to either info about the chosen command or a list of commands. If preceded by an APPEND command with no arguments, appends it instead."

# Testing code
if __name__ == "__main__":
    cmdproc = CmdprocInterpreter()
    print(cmdproc.interpret("FILE-syslib.py|APPEND-NLCRline one NLCR line two-smth else"))