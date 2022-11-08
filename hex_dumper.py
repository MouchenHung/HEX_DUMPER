#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 09:42:43 2022

@author: Mouchen
@discription: Hex dump and search and compare
@note: none
"""
import sys
from lib.common_lib import Common_msg, Common_file
from lib.platform_lib import Platform

APP_NAME = "HEX DUMPER"
APP_AUTH = "Mouchen"
APP_RELEASE_VER = "1.0.1"
APP_RELEASE_DATE = "2022.11.08"

MODE_STANDARD = 0
MODE_SEARCH = 1
MODE_COMPARE = 2

MODE_COMP_ALL = 0
MODE_COMP_DIFF = 1
MODE_COMP_SAME = 2

DISPLAY_HEX_NUM = 16

# import common library
comm_msg = Common_msg()
msg_hdr_print = comm_msg.msg_hdr_print
comm_file = Common_file()
list_rm = comm_file.list_rm
check_hex_valid = comm_file.check_hex_valid
is_binary = comm_file.is_binary
is_file_exist = comm_file.is_file_exist
list_dump = comm_file.list_dump

# import platform library
plat = Platform(DISPLAY_HEX_NUM)

def Search_mode_task(img_path, search_list, force_flag=0):
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
        plat.image_dump(img_path, rec_ofst, len(search_list), force_flag)

def Compare_mode_task(img_path1, img_path2, sub_mode, force_flag=0):
    if sub_mode == MODE_COMP_ALL:
        if force_flag:
            plat.image_dump_two_2(img_path1, img_path2)
        else:
            plat.image_dump_two_1(img_path1, img_path2)
    elif sub_mode == MODE_COMP_DIFF:
        if force_flag:
            plat.image_dump_two_2(img_path1, img_path2, mode="diff")
        else:
            plat.image_dump_two_1(img_path1, img_path2, mode="diff")
    elif sub_mode == MODE_COMP_SAME:
        if force_flag:
            plat.image_dump_two_2(img_path1, img_path2, mode="same")
        else:
            plat.image_dump_two_1(img_path1, img_path2, mode="same")
    else:
        msg_hdr_print("e", "Not support sub-mode ["+ str(sub_mode) +"]")

def APP_HELP():
    msg_hdr_print("n", "--------------------------------------------------", "\n")
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

class APP_ARG():
    def __init__(self, argv):
        self.argv = argv
        self.argc = len(self.argv)
        self.image1_path = ""
        self.image2_path = ""
        self.mode_select = 0
        self.sub_mode_select = 0
        self.filter_ofst = 0
        self.filter_num = -1
        self.force_print_flag = 0
        self.key_lst = []
        self.err_flag = 0

    def arg_parsing(self):
        for i in range(self.argc):
            if self.argv[i] == "-i1" or self.argv[i] == "-i":
                if i+1 < self.argc:
                    if "-" not in self.argv[i+1]:
                        self.image1_path = self.argv[i+1]
                        i+=1

            if self.argv[i] == "-i2":
                if i+1 < self.argc:
                    if "-" not in self.argv[i+1]:
                        self.image2_path = self.argv[i+1]
                        i+=1

            elif self.argv[i] == "-m":
                if i+1 < self.argc:
                    if "-" not in self.argv[i+1]:
                        self.mode_select = int(self.argv[i+1], 10)
                        i+=1

            elif self.argv[i] == "-s":
                if i+1 < self.argc:
                    if "-" not in self.argv[i+1]:
                        self.filter_ofst = int(self.argv[i+1], 16)
                        i+=1

            # Only work in STANDARD_MODE
            elif self.argv[i] == "-n":
                if i+1 < self.argc:
                    if "-" not in self.argv[i+1]:
                        self.filter_num = int(self.argv[i+1], 10)
                        i+=1

            # Only work in SEARCH_MODE/COMPARE_MODE
            elif self.argv[i] == "-f":
                self.force_print_flag = 1

            # Only work in COMPARE_MODE
            elif self.argv[i] == "-c":
                if i+1 < self.argc:
                    if "-" not in self.argv[i+1]:
                        self.sub_mode_select = int(self.argv[i+1], 10)
                        i+=1

            elif self.argv[i] == "-k":
                if i+1 < self.argc:
                    for j in range(i+1, self.argc, 1):
                        if "-" in self.argv[j]:
                            break
                        else:
                            if check_hex_valid(self.argv[j]):
                                msg_hdr_print("e", "Invalid searh byte detect!")
                                self.err_flag = 1
                            else:
                                self.key_lst.append(hex(int(self.argv[j], 16)))

                    if not len(self.key_lst):
                        msg_hdr_print("e", "Search key missing!")
                        self.err_flag = 1

                    i += len(self.key_lst)
                else:
                    msg_hdr_print("e", "Search key missing!")
                    self.err_flag = 1

if __name__ == '__main__':
    # [STEP0] Print app info
    APP_HEADER()

    # [STEP1] Parsing input arg
    app_arg = APP_ARG(sys.argv)
    app_arg.arg_parsing()

    image1_path = app_arg.image1_path
    image2_path = app_arg.image2_path
    mode_select = app_arg.mode_select
    sub_mode_select = app_arg.sub_mode_select
    filter_ofst = app_arg.filter_ofst
    filter_num = app_arg.filter_num
    force_print_flag = app_arg.force_print_flag
    key_lst = app_arg.key_lst
    err_flag = app_arg.err_flag

    # [STEP2] Verify input arg
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

    if image1_path:
        if not is_file_exist(image1_path):
            msg_hdr_print("e", "Image1 is not existed!")
            err_flag = 1
        else:
            if not is_binary(image1_path):
                msg_hdr_print("e", "Image1 is empty or not binary file!")
                err_flag = 1

    if image2_path:
        if not is_file_exist(image2_path):
            msg_hdr_print("e", "Image2 is not existed!")
            err_flag = 1
        else:
            if not is_binary(image2_path):
                msg_hdr_print("e", "Image2 is empty or not binary file!")
                err_flag = 1

    if err_flag:
        APP_HELP()
        sys.exit(0)

    # [STEP3] Start Task
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
            plat.image_dump(image1_path, filter_ofst, filter_num)
        else:
            plat.image_dump(image2_path, filter_ofst, filter_num)

    elif mode_select == MODE_SEARCH:
        msg_hdr_print("c", "* mode:       SEARCH MODE")
        if image1_path != "":
            msg_hdr_print("c", "* image:      " + image1_path)
        else:
            msg_hdr_print("c", "* image:      " + image2_path)
        list_dump(key_lst, "         * search_lst: ")

        if image1_path != "":
            Search_mode_task(image1_path, key_lst, force_print_flag)
        else:
            Search_mode_task(image2_path, key_lst, force_print_flag)

    elif mode_select == MODE_COMPARE:
        msg_hdr_print("c", "* mode:       COMPARE MODE")
        msg_hdr_print("c", "* image1:     " + image1_path)
        msg_hdr_print("c", "* image2:     " + image2_path)

        Compare_mode_task(image1_path, image2_path, sub_mode_select, force_print_flag)
