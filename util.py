import os
from inspect import getsource

import psutil

red = "\033[0;31m"
dark_green = "\033[0;32m"
orange = "\033[0;33m"
dark_blue = "\033[0;34m"
bright_purple = "\033[0;35m"
dark_cyan = "\033[0;36m"
dull_white = "\033[0;37m"
pure_black = "\033[0;30m"
bright_red = "\033[0;91m"
light_green = "\033[0;92m"
yellow = "\033[0;93m"
bright_blue = "\033[0;94m"
purple = "\033[0;95m"
blue = "\033[0;96m"
bright_black = "\033[0;90m"
bright_white = "\033[0;97m"
cyan_back = "\033[0;46m"
purple_back = "\033[0;45m"
white_back = "\033[0;47m"
blue_back = "\033[0;44m"
orange_back = "\033[0;43m"
green_back = "\033[0;42m"
pink_back = "\033[0;41m"
grey_back = "\033[0;40m"
grey = '\033[38;4;236m'
bold = "\033[1m"
underline = "\033[4m"
italic = "\033[3m"
darken = "\033[2m"
invisible = '\033[08m'
reverse_color = '\033[07m'
reset_color = '\033[0m'


def get_process_memory():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()

    return mem_info.rss


def asserter(fn, ev):
    x = fn()
    if x != ev:
        print(f'{red}{getsource(fn)[17:-2]}{reset_color}')
        print(f'Returned:\t{x}')
        print(f'Expected:\t{ev}')
    else:
        print(f'{dark_green}{getsource(fn)[17:-2]}{reset_color}')
