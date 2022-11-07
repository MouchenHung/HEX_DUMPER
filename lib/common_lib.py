import sys

os_name = sys.platform

class bcolors:
    purple = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    lightgray = '\033[97m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def msg_hdr_print(hdr_type, msg, pre_msg="", end_msg="\n"):
    if hdr_type == "s":     #system
        header = "<system> "
    elif hdr_type == "w":   #warning
        header = "<warn> "
    elif hdr_type == "e":   #error
        header = "<error> "
    elif hdr_type == "wdt": #watchdog
        header = "<wdt> "
    elif hdr_type == "n": #none
        header = ""
    elif hdr_type == "c": #none with space front
        header = ""
        pre_msg = "         "
    print(pre_msg + header + msg, end=end_msg)

def msg_color_print(msg, color, end_msg="\n"):
    if os_name == "linux":
        print(color + msg + bcolors.ENDC, end=end_msg)
    else:
        print(msg, end=end_msg)
