import sys
import subprocess
import os

def parse(line):
    command = line.split()
    return command

def mainpoint(execu):
        if execu[0] == "cd":
            folder = os.path.dirname(os.path.abspath(execu[1]))
            path = ("%s/" + execu[1]) % folder
            os.chdir(path)
            return os.getcwd()
        if execu[0] == "ls":
            folder = os.path.dirname(os.path.abspath(execu[1]))
            path = ("%s/" + execu[1]) % folder
            os.chdir(path)
            os.system("ls")



def run(line):
    execu = parse(line)
    if execu:
        return mainpoint(execu)

def main():
    line = raw_input("$")
    status = run(line)
    print status

if __name__ =="__main__":
    main()
