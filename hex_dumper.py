#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 09:42:43 2022

@author: Mouchen
@discription: Hex dump and search and compare
@note: 
"""
from email import header
import os, sys
from traceback import print_tb
import lib.common_lib as common
from lib.common_lib import msg_hdr_print, msg_color_print

APP_NAME = "HEX DUMPER"
APP_AUTH = "Mouchen"
APP_RELEASE_VER = "1.0.0"
APP_RELEASE_DATE = "2022.11.04"

MODE_STANDARD = 0
MODE_SEARCH = 1
MODE_COMPARE = 2

DISPLAY_HEX_NUM = 16

def list_dump(list, pre_msg=""):
    print(pre_msg + "[", end="")
    for i in range(len(list)):
        if i == len(list)-1:
            print(list[i].replace("0x", ""), end="")
        else:
            print(list[i].replace("0x", ""), end=", ")
    print("]")

def image_dump_two_1(img_path1, img_path2, rec_ofst=0, rec_num=-1, mode="all"):
    img1_data = []
    img2_data = []
    with open(img_path1,"rb") as f:
        img1_data = f.read()

    with open(img_path2,"rb") as f:
        img2_data = f.read()

    rec_remain = rec_num

    ofst = int(rec_ofst / DISPLAY_HEX_NUM) * DISPLAY_HEX_NUM
    end_flag = [0,0]

    empty_str = ""
    for i in range(int(DISPLAY_HEX_NUM/2)):
        empty_str += "~~"
        empty_str += " "
    empty_str += "  "
    for i in range(int(DISPLAY_HEX_NUM/2)):
        empty_str += "~~"
        empty_str += " "

    print("\n           ", end='')
    for i in range(DISPLAY_HEX_NUM):
        if i == int(DISPLAY_HEX_NUM/2):
            print("", end='  ')
        print(str(i).rjust(2,'0'), end=' ')
    print("      ", end='')
    for i in range(DISPLAY_HEX_NUM):
        if i == int(DISPLAY_HEX_NUM/2):
            print("", end='  ')
        print(str(i).rjust(2,'0'), end=' ')
    print("\n-------------------------------------------------------------------------------------------------------------------")
    while(1):
        # check remain record data number
        if rec_remain == 0 and rec_num != -1:
            break

        cur_line_hdr = ""
        line_hdr = hex(ofst).replace("0x", "").rjust(8, '0')
        cur_line_hdr += line_hdr
        cur_line_hdr += "   "

        img1_area = ""
        for i in range(ofst, ofst+DISPLAY_HEX_NUM, 1):
            if i == ofst + int(DISPLAY_HEX_NUM/2):
                img1_area += "  "
            if i >= len(img1_data):
                img1_area += "~~ "
                end_flag[0] = 1
                continue
            if mode == "all":
                img1_area += hex(img1_data[i]).replace("0x", "").rjust(2, '0')
            elif mode == "same":
                if i >= len(img2_data):
                    img1_area += "~~ "
                    continue
                if img1_data[i] == img2_data[i]:
                    img1_area += hex(img1_data[i]).replace("0x", "").rjust(2, '0')
                else:
                    img1_area += "~~"
            elif mode == "diff":
                if i >= len(img2_data):
                    img1_area += "~~ "
                    continue
                if img1_data[i] != img2_data[i]:
                    img1_area += hex(img1_data[i]).replace("0x", "").rjust(2, '0')
                else:
                    img1_area += "~~"
            img1_area += " "

        img2_area = ""
        for i in range(ofst, ofst+DISPLAY_HEX_NUM, 1):
            if i == ofst + int(DISPLAY_HEX_NUM/2):
                img2_area += "  "
            if i >= len(img2_data):
                img2_area += "~~ "
                end_flag[1] = 1
                continue
            if mode == "all":
                img2_area += hex(img2_data[i]).replace("0x", "").rjust(2, '0')
            elif mode == "same":
                if i >= len(img1_data):
                    img2_area += "~~ "
                    continue
                if img1_data[i] == img2_data[i]:
                    img2_area += hex(img2_data[i]).replace("0x", "").rjust(2, '0')
                else:
                    img2_area += "~~"
            elif mode == "diff":
                if i >= len(img1_data):
                    img2_area += "~~ "
                    continue
                if img1_data[i] != img2_data[i]:
                    img2_area += hex(img2_data[i]).replace("0x", "").rjust(2, '0')
                else:
                    img2_area += "~~"
            img2_area += " "

        # Skip print if not meet required status
        if img1_area != empty_str and img2_area != empty_str:
            print(cur_line_hdr, end='')
            print(img1_area, end='')
            print("     ", end='')
            print(img2_area)

        if end_flag[0] and end_flag[1]:
            break

        ofst += DISPLAY_HEX_NUM

    print("-------------------------------------------------------------------------------------------------------------------")

def color_split_print(hex_data, focus_lst, ofst):
    for i in range(ofst, ofst+DISPLAY_HEX_NUM, 1):
        if i == ofst + int(DISPLAY_HEX_NUM/2):
            print("  ", end="")
        if i in focus_lst:
            msg_color_print(hex(hex_data[i]).replace("0x", "").rjust(2, '0'), common.bcolors.red, " ")
        else:
            print(hex(hex_data[i]).replace("0x", "").rjust(2, '0'), end=" ")

def image_dump_two_2(img_path1, img_path2, rec_ofst=0, rec_num=-1, mode="all"):
    img1_data = []
    img2_data = []
    with open(img_path1,"rb") as f:
        img1_data = f.read()

    with open(img_path2,"rb") as f:
        img2_data = f.read()

    rec_remain = rec_num

    ofst = int(rec_ofst / DISPLAY_HEX_NUM) * DISPLAY_HEX_NUM
    end_flag = [0,0]

    empty_str = ""
    for i in range(int(DISPLAY_HEX_NUM/2)):
        empty_str += "~~"
        empty_str += " "
    empty_str += "  "
    for i in range(int(DISPLAY_HEX_NUM/2)):
        empty_str += "~~"
        empty_str += " "

    print("\n           ", end='')
    for i in range(DISPLAY_HEX_NUM):
        if i == int(DISPLAY_HEX_NUM/2):
            print("", end='  ')
        print(str(i).rjust(2,'0'), end=' ')
    print("      ", end='')
    for i in range(DISPLAY_HEX_NUM):
        if i == int(DISPLAY_HEX_NUM/2):
            print("", end='  ')
        print(str(i).rjust(2,'0'), end=' ')
    print("\n-------------------------------------------------------------------------------------------------------------------")
    while(1):
        # check remain record data number
        if rec_remain == 0 and rec_num != -1:
            break

        cur_line_hdr = ""
        line_hdr = hex(ofst).replace("0x", "").rjust(8, '0')
        cur_line_hdr += line_hdr
        cur_line_hdr += "   "

        img1_focus = []
        for i in range(ofst, ofst+DISPLAY_HEX_NUM, 1):
            if i >= len(img1_data):
                end_flag[0] = 1
                continue
            if mode == "all":
                img1_focus.append(i)
            elif mode == "same":
                if i >= len(img2_data):
                    continue
                if img1_data[i] == img2_data[i]:
                    img1_focus.append(i)
            elif mode == "diff":
                if i >= len(img2_data):
                    img1_focus.append(i)
                    continue
                if img1_data[i] != img2_data[i]:
                    img1_focus.append(i)

        img2_focus = []
        for i in range(ofst, ofst+DISPLAY_HEX_NUM, 1):
            if i >= len(img2_data):
                end_flag[1] = 1
                continue
            if mode == "all":
                img2_focus.append(i)
            elif mode == "same":
                if i >= len(img1_data):
                    continue
                if img1_data[i] == img2_data[i]:
                    img2_focus.append(i)
            elif mode == "diff":
                if i >= len(img1_data):
                    img2_focus.append(i)
                    continue
                if img1_data[i] != img2_data[i]:
                    img2_focus.append(i)

        # Skip print if not meet required status
        if len(img1_focus) and len(img2_focus):
            print(cur_line_hdr, end='')
            color_split_print(img1_data, img1_focus, ofst)
            print("     ", end='')
            color_split_print(img2_data, img2_focus, ofst)
            print("")

        if end_flag[0] and end_flag[1]:
            break

        ofst += DISPLAY_HEX_NUM
    
    print("-------------------------------------------------------------------------------------------------------------------")
    print("image1 size: ", hex(len(img1_data)).rjust(8, '0'))
    print("image2 size: ", hex(len(img2_data)).rjust(8, '0'))

def image_dump(img_path, rec_ofst=0, rec_num=-1):
    with open(img_path,"rb") as f:
        data = f.read()

        if rec_num == -1:
            rec_num = len(data)

        ofst = int(rec_ofst / DISPLAY_HEX_NUM) * DISPLAY_HEX_NUM

        end_flag = 0
        rec_remain = rec_num

        print("\n           ", end='')
        for i in range(DISPLAY_HEX_NUM):
            if i == int(DISPLAY_HEX_NUM/2):
                print("", end='  ')
            print(str(i).rjust(2,'0'), end=' ')
        print("\n------------------------------------------------------------")
        while(1):
            # check remain record data number
            if rec_remain == 0:
                break

            if ofst + DISPLAY_HEX_NUM < len(data):
                display_num = DISPLAY_HEX_NUM
            else:
                display_num = len(data) - ofst
                end_flag = 1

            print(hex(ofst).replace("0x", "").rjust(8, '0'), end='   ')
            for i in range(ofst, ofst+display_num, 1):
                if i == ofst + int(DISPLAY_HEX_NUM/2):
                    print("", end='  ')
                if (i >= rec_ofst and rec_remain != 0):
                    print(hex(data[i]).replace("0x", "").rjust(2, '0'), end=' ')
                    rec_remain -= 1
                else:
                    print("  ", end=' ')
            print("")

            if end_flag:
                break

            ofst += DISPLAY_HEX_NUM
        print("------------------------------------------------------------")

def is_file_exist(file_path):
    if not os.path.exists(file_path):
        return False
    else:
        return True

def is_binary(file_path):
    try:
        with open(file_path, 'tr') as check_file:
            check_file.read()
            return 0
    except:
        return os.path.getsize(file_path)

def byte_to_k(byte_num):
    return round(byte_num/1024)

def gen_bytes(num, pad_size, pad_val_str, mode):
    hex_str = str(hex(num))
    hex_str = hex_str.replace("0x", "")

    output = []
    if not pad_size:
        return output
    
    if ( len(hex_str) ) > pad_size*2:
        return output

    # padding
    if len(hex_str) != pad_size*2:
        hex_str = pad_val_str*(pad_size*2 - len(hex_str)) + hex_str
    
    if mode == "msb":
        for i in range( 0, len(hex_str), 2 ):
            output.append( int(hex_str[i]+hex_str[i+1], 16) )
    elif mode == "lsb":
        for i in range( len(hex_str)-1, 0, -2 ):
            output.append( int(hex_str[i-1]+hex_str[i], 16) )
    
    return output

def check_hex_valid(hex_str):
    if int(hex_str, 16) > 0xff or int(hex_str, 16) < 0:
        return 1
    return 0

def list_rm(list, idx=-1):
    if (len(list) == 0):
        return list
    
    if idx == -1:
        rm_idx = len(list) - 1
    else:
        if idx < 0 or idx > len(list)-1:
            print("Invalid index given")
            return list
        rm_idx = idx

    new_lst = []
    for i in range(len(list)):
        if i == rm_idx:
            continue
        new_lst.append(list[i])

    return new_lst

def Search_mode_task(img_path, search_list):
    combo_flag = 0
    rec_ofst_lst = []
    rec_idx = 0
    with open(img_path,"rb") as f:
        data = f.read()

        for i in range(len(data)):
            if combo_flag == 1:
                if (hex(data[i]) == search_list[rec_idx]):
                    rec_idx += 1
                    if rec_idx == len(search_list):
                        combo_flag = 0
                else:
                    if rec_idx != len(search_list):
                        rec_ofst_lst = list_rm(rec_ofst_lst)
                    combo_flag = 0
            else:
                rec_idx = 0
                if (hex(data[i]) == search_list[rec_idx]):
                    rec_ofst_lst.append(i)
                    combo_flag = 1
                    rec_idx += 1

    for rec_ofst in rec_ofst_lst:
        image_dump(img_path, rec_ofst, len(search_list))

def Compare_mode_task(img_path1, img_path2, sub_mode, force_flag):
    if sub_mode == 0:
        if force_flag:
            image_dump_two_2(img_path1, img_path2)
        else:
            image_dump_two_1(img_path1, img_path2)
    elif sub_mode == 1:
        if force_flag:
            image_dump_two_2(img_path1, img_path2, mode="diff")
        else:
            image_dump_two_1(img_path1, img_path2, mode="diff")
    elif sub_mode == 2:
        if force_flag:
            image_dump_two_2(img_path1, img_path2, mode="same")
        else:
            image_dump_two_1(img_path1, img_path2, mode="same")
    else:
        msg_hdr_print("e", "Not support sub-mode ["+ str(sub_mode) +"]")

def APP_HELP():
    msg_hdr_print("n", "--------------------------------------------------")
    msg_hdr_print("n", "HELP:")
    msg_hdr_print("n", "-i1/-i  Image1 path")
    msg_hdr_print("n", "-i2     Image2 path")
    msg_hdr_print("n", "-m      Selet mode.")
    msg_hdr_print("n", "          [0] STANDARD_MODE")
    msg_hdr_print("n", "          [1] SEARCH_MODE")
    msg_hdr_print("n", "          [2] COMPARE_MODE")
    msg_hdr_print("n", "        note: Default is STANDARD_MODE")
    msg_hdr_print("n", "-k      Hex list in SEARCH_MODE")
    msg_hdr_print("n", "        note: Only work in SEARCH_MODE")
    msg_hdr_print("n", "-s      Display offset")
    msg_hdr_print("n", "        note: Only work in STANDARD_MODE")
    msg_hdr_print("n", "-n      Display numbers of bytes")
    msg_hdr_print("n", "        note: Only work in STANDARD_MODE")
    msg_hdr_print("n", "-f      Force to print all element")
    msg_hdr_print("n", "        note: Only work in SEARCH_MODE/COMPARE_MODE and only support in LINUX")
    msg_hdr_print("n", "-c      Choose sub mode")
    msg_hdr_print("n", "        note: Only work in COMPARE_MODE, default 0")
    msg_hdr_print("n", "          * COMPARE_MODE")
    msg_hdr_print("n", "            [0] no filter (default)")
    msg_hdr_print("n", "            [1] find different")
    msg_hdr_print("n", "            [2] find same")
    msg_hdr_print("n", "")
    msg_hdr_print("n", "Ex: STANDARD MODE:")
    msg_hdr_print("n", "    ./hex_dumper -i <image_path> -s <ofset> -n <num>")
    msg_hdr_print("n", "Ex: SEARCH MODE:")
    msg_hdr_print("n", "    ./hex_dumper -m 1 -i <image_path> -k <list of bytes>")
    msg_hdr_print("n", "Ex: COMPARE MODE: find same")
    msg_hdr_print("n", "    ./hex_dumper -m 2 -c 1 -i1 <image1_path> -i2 <image2_path>")
    msg_hdr_print("n", "Ex: COMPARE MODE: find different")
    msg_hdr_print("n", "    ./hex_dumper -m 2 -c 2 -i1 <image1_path> -i2 <image2_path>")
    msg_hdr_print("n", "--------------------------------------------------")

def APP_HEADER():
    msg_hdr_print("n", "========================================================")
    msg_hdr_print("n", "* APP name:    "+APP_NAME)
    msg_hdr_print("n", "* APP auth:    "+APP_AUTH)
    msg_hdr_print("n", "* APP version: "+APP_RELEASE_VER)
    msg_hdr_print("n", "* APP date:    "+APP_RELEASE_DATE)
    msg_hdr_print("n", "========================================================")

if __name__ == '__main__':
    APP_HEADER()

    argc = len(sys.argv)

    image1_path = ""
    image2_path = ""
    mode_select = 0
    sub_mode_select = 0
    filter_ofst = 0
    filter_num = -1
    force_print_flag = 0
    key_lst = []

    err_flag = 0
    input_lst = []
    for i in range(argc):
        if sys.argv[i] == "-i1" or sys.argv[i] == "-i":
            if i+1 < argc:
                if "-" not in sys.argv[i+1]:
                    image1_path = sys.argv[i+1]
                    i+=1

        if sys.argv[i] == "-i2":
            if i+1 < argc:
                if "-" not in sys.argv[i+1]:
                    image2_path = sys.argv[i+1]
                    i+=1

        elif sys.argv[i] == "-m":
            if i+1 < argc:
                if "-" not in sys.argv[i+1]:
                    mode_select = int(sys.argv[i+1], 10)
                    i+=1

        elif sys.argv[i] == "-s":
            if i+1 < argc:
                if "-" not in sys.argv[i+1]:
                    filter_ofst = int(sys.argv[i+1], 16)
                    i+=1

        # Only work in STANDARD_MODE
        elif sys.argv[i] == "-n":
            if i+1 < argc:
                if "-" not in sys.argv[i+1]:
                    filter_num = int(sys.argv[i+1], 10)
                    i+=1

        # Only work in COMPARE_MODE
        elif sys.argv[i] == "-f":
            force_print_flag = 1

        # Only work in COMPARE_MODE
        elif sys.argv[i] == "-c":
            if i+1 < argc:
                if "-" not in sys.argv[i+1]:
                    sub_mode_select = int(sys.argv[i+1], 10)
                    i+=1
        
        elif sys.argv[i] == "-k":
            if i+1 < argc:
                for j in range(i+1, argc, 1):
                    if "-" in sys.argv[j]:
                        break
                    else:
                        if check_hex_valid(sys.argv[j]):
                            msg_hdr_print("e", "Invalid searh byte detect!")
                            err_flag = 1
                        else:
                            key_lst.append(hex(int(sys.argv[j], 16)))

                if not len(key_lst):
                    msg_hdr_print("e", "Search key missing!")
                    err_flag = 1

                i += len(key_lst)
            else:
                msg_hdr_print("e", "Search key missing!")
                err_flag = 1
            
    
    if mode_select == MODE_STANDARD:
        if image1_path == "" and image2_path == "":
            msg_hdr_print("e", "STANDARD_MODE should given at least 1 image!")
            err_flag = 1
        elif image1_path and image2_path:
            msg_hdr_print("e", "STANDARD_MODE should only given 1 image!")
            err_flag = 1
    elif mode_select == MODE_SEARCH:
        if image1_path == "" and image2_path == "":
            msg_hdr_print("e", "SEARCH_MODE should given at least 1 image!")
            err_flag = 1
        elif image1_path and image2_path:
            msg_hdr_print("e", "SEARCH_MODE should only given 1 image!")
            err_flag = 1
    elif mode_select == MODE_COMPARE:
        if image1_path == "" or image2_path == "":
            msg_hdr_print("e", "COMPARE_MODE should given 2 images!")
            err_flag = 1
    else:
        msg_hdr_print("e", "Unsupported mode!")
        err_flag = 1

    if err_flag:
        APP_HELP()
        sys.exit(0)

    msg_hdr_print("s", "Config set:")
    if mode_select == MODE_STANDARD:
        msg_hdr_print("c", "* mode:       STANDARD MODE")
        if image1_path != "":
            msg_hdr_print("c", "* image:      " + image1_path)
        else:
            msg_hdr_print("c", "* image:      " + image2_path)
        msg_hdr_print("c", "* ofset:      " + hex(filter_ofst))
        if filter_num == -1:
            msg_hdr_print("c", "* number:     all")
        else:
            msg_hdr_print("c", "* number:     " + str(filter_num))
        
        if image1_path != "":
            image_dump(image1_path, filter_ofst, filter_num)
        else:
            image_dump(image2_path, filter_ofst, filter_num)

    elif mode_select == MODE_SEARCH:
        msg_hdr_print("c", "* mode:       SEARCH MODE")
        if image1_path != "":
            msg_hdr_print("c", "* image:      " + image1_path)
        else:
            msg_hdr_print("c", "* image:      " + image2_path)
        list_dump(key_lst, "         * search_lst: ")

        if image1_path != "":
            Search_mode_task(image1_path, key_lst)
        else:
            Search_mode_task(image2_path, key_lst)

    elif mode_select == MODE_COMPARE:
        msg_hdr_print("c", "* mode:       COMPARE MODE")
        msg_hdr_print("c", "* image1:     " + image1_path)
        msg_hdr_print("c", "* image2:     " + image2_path)

        Compare_mode_task(image1_path, image2_path, sub_mode_select, force_print_flag)
