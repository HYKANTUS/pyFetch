# # # # # # # # # # # # #
#       IMPORTS         #
# # # # # # # # # # # # #
from time import sleep
import os
import platform
import ascii

print()

# # # # # # # # # # # # #
#         INFO          #
# # # # # # # # # # # # #

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
        print('python script written by HYKANTUS')
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
        print(open(__file__).read())

    # general commands
    elif cmd == 'cmd':
        print('run command prompt commands through pyCMD. \nType "exit" to stop\n')
        while True:
            cmdIn = input('cmd > ')
            os.system(cmdIn)

            if cmdIn == 'exit':
                break

    elif cmd == 'osinfo':
        print('-        Operating System Information        -')
        print('name:            ', platform.system())
        print('version:         ', platform.system(), platform.release(), f' ({platform.version()})')
        print()
        print('-            Computer information            -')
        print('architecture:    ', platform.machine())
        print('processor:       ',platform.processor())

    elif cmd == 'osASCII':
        os = platform.system()

        if os.startswith('Windows'):
            url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Windows_logo_-_2012_%28dark_blue%29.svg/1200px-Windows_logo_-_2012_%28dark_blue%29.svg.png'

        if os.startswith('Linux'):
            url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Tux-simple.svg/154px-Tux-simple.svg.png'

        if os.startswith('Mac'):
            url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Apple_logo_black.svg/1010px-Apple_logo_black.svg.png'

        output = ascii.loadFromUrl(url, color=False)
        print(output)

    elif cmd == 'osfetch':
        os = platform.system()

        if os.startswith('Windows'):
            url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Windows_logo_-_2012_%28dark_blue%29.svg/1200px-Windows_logo_-_2012_%28dark_blue%29.svg.png'

        if os.startswith('Linux'):
            url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Tux-simple.svg/154px-Tux-simple.svg.png'

        if os.startswith('Mac'):
            url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Apple_logo_black.svg/1010px-Apple_logo_black.svg.png'

        output = ascii.loadFromUrl(url, color=False)
        print(output)
        print()

        print('-        Operating System Information        -')
        print('name:            ', platform.system())
        print('version:         ', platform.system(), platform.release(), f' ({platform.version()})')
        print()
        print('-            Computer information            -')
        print('architecture:    ', platform.machine())
        print('processor:       ',platform.processor())


# # # # # # # # # # # # #
#          RUN          #
# # # # # # # # # # # # #
while True:
    main()
