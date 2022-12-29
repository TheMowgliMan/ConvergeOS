# cmdlib.py
# This file has the command functions.
# Author: @TheMowgliMan
# Other Contributors:


from syslib import reassemble
import cmdproc
import warnings


# Stores help values for commands
help_dict = {
    "echo":"Echo <cmdproc (optional)>:bool <log (optional)>:bool <inputs>:string: Prints its inputs to the terminal. Supports cmdproc\nwith cmdproc at <cmdproc>. Logs into 'echolog.txt' if 'log' added after <cmdproc> but before otehr inputs.",
    "eval":"Eval <python>:string: Evaluates a line of Python. Does not support cmdproc.",
    "exit":"Exit: Forcibly terminates the OS. May cause errors when using multiprocess.",
    "help":"Help <command (optional)>:string: Prints a list of all commands, or when given inputs gives defenitions for each command."
}


# Prints a string or list to stdout; raises error if wrong type.
def echo(text):
    if isinstance(text, str):
        print(text)
    elif isinstance(text, list):
        if text[0] == "cmdproc":
            cmd = cmdproc.CmdprocInterpreter()
            inp = text
            del inp[0]

            if inp[0] == "log":
                del inp[0]

                f = open("echolog.txt", 'a')

                out = cmd.interpret(reassemble(inp))

                f.write("\n" + out + "\n")
                f.close()
                print(out)
            else:
                out = cmd.interpret(reassemble(inp))
                print(out)
        else:
            inp = text
            if inp[0] == "log":
                del inp[0]

                f = open("echolog.txt", 'a')

                out = reassemble(inp, filter_str=True)

                f.write("\n" + out + "\n")
                f.close()
                print(out)
            else:
                out = reassemble(inp, filter_str=True)
                print(out)
    else:
        raise TypeError("Echo only takes a string or list!")

# Evaluates a single line of python
def evaluate(text):
    if isinstance(text, list):
        try:
            ret = eval(reassemble(text).strip())
            print(ret)
        except SyntaxError:
            print("Command '" + reassemble(text).strip() + "' has incorrect syntax.")
    else:
        raise TypeError("Eval only takes a string or list!")

# Exits the OS
def exit_os(inputs):
    if inputs != []:
        print("Note: Exit uses no inputs.")

    print("Note that Exit forcibly closes the OS! Any running programs in the background will be forcibly terminated.")

    print("Exiting...")

    exit()

# Help function
def help_cmd(inputs):
    if inputs == []:
        print("All commands:", "echo", "eval", "exit", "help", sep="\n")
    else:
        for i in inputs:
            if i in help_dict:
                print(help_dict[i])
            else:
                print(str(i).capitalize() + ": This command does not exist.")

def process_command(command, input):
    if command == "echo":
        echo(input)
    elif command == "eval":
        evaluate(input)
    elif command == "exit":
        exit_os(input)
    elif command == "help":
        help_cmd(input)
    else:
        warnings.warn("Command " + command + " does not exist.")
