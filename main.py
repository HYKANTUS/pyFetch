# # # # # # # # # # # # #
#       IMPORTS         #
# # # # # # # # # # # # #
from time import sleep
import os
import platform
import pyASCIIgenerator

# # # # # # # # # # # # #
#         INFO          #
# # # # # # # # # # # # #
logofile = open('logo.txt', 'r')
logolines = logofile.readlines()

for line in logolines:
    print("{}".format(line.strip()))

print('pyCMD by HYKANTUS')

information = '"help", "credits", or "license"'

print(f'Type {information} for more information.\n')


# # # # # # # # # # # # #
#        COMMANDS       #
# # # # # # # # # # # # #
def main():
    # pyCMD input
    cmd = input('>>> ')

    # information commands
    if cmd == 'help':
        helpfile = open('help.txt', 'r')
        helplines = helpfile.readlines()

        for line in helplines:
            print("{}".format(line.strip()))

        print()

    elif cmd == 'credits':
        print('python script written by HYKANTUS. \nGithub repository: https://github.com/HYKANTUS/pyCMD')
        print()

    elif cmd == 'license':
        print()

        licensefile = open('LICENSE', 'r')
        licenselines = licensefile.readlines()

        for line in licenselines:
            print("{}".format(line.strip()))

        print()

    # main commands
    elif cmd == 'exit':
        print('exiting... ')
        exit()

    elif cmd == 'srccode':
        print('=========================')
        print(open(__file__).read())
        print('=========================')
        print('Github repository: https://github.com/HYKANTUS/pyCMD')

    # os commands
    elif cmd == 'osinfo':
        print('-        Operating System Information        -')
        print('name:            ', platform.system())
        print('version:         ', platform.system(), platform.release(), f' ({platform.version()})')
        print()
        print('-            Computer information            -')
        print('architecture:    ', platform.machine())
        print('processor:       ', platform.processor())
        print()

    elif cmd == 'osASCII':
        os = platform.system()

        if os.startswith('Windows'):
            filepath = 'osImages\\windows.png'

        if os.startswith('Mac'):
            filepath = 'osImages\\mac.png'

        if os.startswith('Linux'):
            filepath = 'osImages\\linux.png'

        pyASCIIgenerator.asciify(filepath)
        print()

    elif cmd == 'osASCII -windows':
        filepath = 'osImages\\windows.png'
        pyASCIIgenerator.asciify(filepath)
        print()

    elif cmd == 'osASCII -linux':
        filepath = 'osImages\\linux.png'
        pyASCIIgenerator.asciify(filepath)
        print()

    elif cmd == 'osASCII -mac':
        filepath = 'osImages\\mac.png'
        pyASCIIgenerator.asciify(filepath)
        print()

    elif cmd == 'osfetch':
        os = platform.system()

        if os.startswith('Windows'):
            filepath = 'osImages\\windows.png'

        if os.startswith('Linux'):
            filepath = 'osImages\\linux.png'

        if os.startswith('Mac'):
            filepath = 'osImages\\mac.png'

        pyASCIIgenerator.asciify(filepath)
        print()

        print('-        Operating System Information        -')
        print('name:            ', platform.system())
        print('version:         ', platform.system(), platform.release(), f' ({platform.version()})')
        print()
        print('-            Computer information            -')
        print('architecture:    ', platform.machine())
        print('processor:       ', platform.processor())
        print()

    # general commands
    elif cmd == 'cmd':
        from os import system

        print()
        print(
            'run command prompt commands through pyCMD. \nTYPE "cmd" AGAIN TO CONTINUE. \nTYPE "exit" TWICE TO LEAVE THE COMMAND PROMPT. \n')

        while True:
            cmdIn = input('cmd > ')
            system(cmdIn)

            if cmdIn == 'exit':
                break


# # # # # # # # # # # # #
#          RUN          #
# # # # # # # # # # # # #
while True:
    main()
