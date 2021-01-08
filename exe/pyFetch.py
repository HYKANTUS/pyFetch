# # # # # # # # # # # # #
#       IMPORTS         #
# # # # # # # # # # # # #
import os
import platform
import pyASCIIgenerator
import sys

# # # # # # # # # # # # #
#         INFO          #
# # # # # # # # # # # # #
print("""_______   ____    ____     _______  _______  ____________   ______  __    __
|   _  \  \   \  /   /    |   ____||   ____||            | /      ||  |  |  |
|  |_)  |  \   \/   /     |  |__   |  |__    ----|  |---- |  ,----'|  |__|  |
|   ___/    \_    _/      |   __|  |   __|       |  |     |  |     |   __   |
|  |          |  |        |  |     |  |____      |  |     |  `----||  |  |  |
|__|          |__|        |__|     |_______|     |__|      \______||__|  |__|""")

print('pyFetch by HYKANTUS')

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
        print("""All available commands:

-                                  information commands                                    -
help                                    shows this command
credits                                 shows contributors

-                                  main commands                                           -
exit                                    stops running pyFetch
srccode                                 shows all code

-                                  general commands                                        -
osinfo                                  get general information about your computer
osASCII [-windows, -linux]              get an ASCII image of your operating system's image
osfetch                                 combination of osinfo and osASCII

""")

        print()

    elif cmd == 'credits':
        print('python script written by HYKANTUS. \nGithub repository: https://github.com/HYKANTUS/pyCMD')
        print()

    elif cmd == 'license':
        print()
        print("""MIT License

Copyright (c) 2021 HYKANTUS

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
""")

        print()

    # main commands
    elif cmd == 'exit':
        print('exiting... ')
        sys.exit()

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

# # # # # # # # # # # # #
#          RUN          #
# # # # # # # # # # # # #
while True:
    main()
