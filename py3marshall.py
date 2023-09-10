#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# marshal py3

try:
    import os, sys, time, marshal
    import questionary
    from colorama import init, Fore
except Exception as F:
    exit("[ModuleErr] %s" % (F))

if sys.version[0] in '2':
    exit("[sorry] use python version 3")

# Initialisez colorama
init(autoreset=True)

# Couleurs
color_reset = Fore.RESET
color_yellow = Fore.LIGHTYELLOW_EX
color_white = Fore.LIGHTWHITE_EX
color_red = Fore.LIGHTRED_EX

bannerpy3 = """
         {}___
{} ___    |{}_ {} | {}Modder  {}:{} trhacknon
{}| . | | |{}_  {}{}| {}Code    {}:{} Python
{}|  _|_  |{}___{}{}| {}Version {}:{} v.5.0
{}|_| |___| {}*{} https://github.com/tucommenceapousser
""".format(Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.LIGHTCYAN_EX, Fore.RESET, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.LIGHTCYAN_EX, Fore.RESET, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.LIGHTCYAN_EX, Fore.RESET, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.RESET, Fore.RESET, Fore.RED, Fore.RESET)

os.system('clear')
try:
    print(bannerpy3)
    print(f'Input your file location:')
    file = input()
    print(f'Input the output file name (without .py):')  # Demander le nom du fichier de sortie
    output_name = input()
    o = f"{output_name}.py"  # Utiliser le nom du fichier de sortie
except KeyboardInterrupt:
    sys.exit()
else:
    try:
        strng = open(file, 'r').read()
    except IOError:
        print(f'{color_red}\n [' + color_white + '!' + color_red + '] ' + color_red + '[ ' + color_white + 'Error ' + color_red + '] ' + color_white + 'No such file or directory ' + color_red + ': ' + color_white + '"{dfv}"\n')
        sys.exit()
    try:
        code = compile(strng, '', 'exec')
        data = marshal.dumps(code)
    except TypeError:
        print(f'{color_red}   [' + color_white + '!' + color_red + '] ' + color_red + '[ ' + color_white + 'File already to compiled\n')
        sys.exit()

fileout = open(o, 'w')  # Utiliser le nom du fichier de sortie
fileout.write('#Compiled By Trhacknon\n')
fileout.write('#https://github.com/tucommenceapousser\n')
fileout.write('import marshal\n')
fileout.write('exec(marshal.loads(' + repr(data) + '))')
fileout.close()
time.sleep(3)
print(f'{color_yellow}\n [' + color_white + '+' + color_yellow + '] ' + color_white + 'File succes to compile   ' + color_yellow + ': ' + color_white + o + '\n')