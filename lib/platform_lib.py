#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 09:42:43 2022

@author: Mouchen
@discription: platform code
@note: none
"""

from lib.common_lib import Common_msg

# import common lib
com_msg = Common_msg()
msg_hdr_print = com_msg.msg_hdr_print
msg_color_print = com_msg.msg_color_print

class Platform:
    def __init__(self, _display_hex_num):
        # How many bytes should display in one line
        self.display_hex_num = _display_hex_num

    # Dump 1 images
    def image_dump(self, img_path, rec_ofst=0, rec_num=-1, force_flag=0):
        with open(img_path,"rb") as f:
            data = f.read()

            if rec_num == -1:
                rec_num = len(data)

            ofst = int(rec_ofst / self.display_hex_num) * self.display_hex_num

            end_flag = 0
            rec_remain = rec_num

            print("\n           ", end='')
            for i in range(self.display_hex_num):
                if i == int(self.display_hex_num/2):
                    print("", end='  ')
                print(str(i).rjust(2,'0'), end=' ')
            print("\n------------------------------------------------------------")
            while(1):
                # check remain record data number
                if rec_remain == 0:
                    break

                if ofst + self.display_hex_num < len(data):
                    display_num = self.display_hex_num
                else:
                    display_num = len(data) - ofst
                    end_flag = 1

                print(hex(ofst).replace("0x", "").rjust(8, '0'), end='   ')
                for i in range(ofst, ofst+display_num, 1):
                    if i == ofst + int(self.display_hex_num/2):
                        print("", end='  ')
                    if (i >= rec_ofst and rec_remain != 0):
                        if force_flag:
                            msg_color_print(hex(data[i]).replace("0x", "").rjust(2, '0'), com_msg.color_red, " ")
                        else:
                            print(hex(data[i]).replace("0x", "").rjust(2, '0'), end=' ')
                        rec_remain -= 1
                    else:
                        if force_flag:
                            print(hex(data[i]).replace("0x", "").rjust(2, '0'), end=' ')
                        else:
                            print("  ", end=' ')
                print("")

                if end_flag:
                    break

                ofst += self.display_hex_num
            print("------------------------------------------------------------")
            print("image size: ", hex(len(data)).rjust(8, '0'))

    # Dump 2 images without color
    def image_dump_two_1(self, img_path1, img_path2, rec_ofst=0, rec_num=-1, mode="all"):
        img1_data = []
        img2_data = []
        with open(img_path1,"rb") as f:
            img1_data = f.read()

        with open(img_path2,"rb") as f:
            img2_data = f.read()

        rec_remain = rec_num

        ofst = int(rec_ofst / self.display_hex_num) * self.display_hex_num
        end_flag = [0,0]

        empty_str = ""
        for i in range(int(self.display_hex_num/2)):
            empty_str += "~~"
            empty_str += " "
        empty_str += "  "
        for i in range(int(self.display_hex_num/2)):
            empty_str += "~~"
            empty_str += " "

        print("\n           ", end='')
        for i in range(self.display_hex_num):
            if i == int(self.display_hex_num/2):
                print("", end='  ')
            print(str(i).rjust(2,'0'), end=' ')
        print("      ", end='')
        for i in range(self.display_hex_num):
            if i == int(self.display_hex_num/2):
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
            for i in range(ofst, ofst+self.display_hex_num, 1):
                if i == ofst + int(self.display_hex_num/2):
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
            for i in range(ofst, ofst+self.display_hex_num, 1):
                if i == ofst + int(self.display_hex_num/2):
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

            ofst += self.display_hex_num

        print("-------------------------------------------------------------------------------------------------------------------")
        print("image1 size: ", hex(len(img1_data)).rjust(8, '0'))
        print("image2 size: ", hex(len(img2_data)).rjust(8, '0'))

    def color_split_print(self, hex_data, focus_lst, ofst):
        for i in range(ofst, ofst+self.display_hex_num, 1):
            if i == ofst + int(self.display_hex_num/2):
                print("  ", end="")
            if i in focus_lst:
                msg_color_print(hex(hex_data[i]).replace("0x", "").rjust(2, '0'), com_msg.color_red, " ")
            else:
                print(hex(hex_data[i]).replace("0x", "").rjust(2, '0'), end=" ")

    # Dump 2 images with color
    def image_dump_two_2(self, img_path1, img_path2, rec_ofst=0, rec_num=-1, mode="all"):
        img1_data = []
        img2_data = []
        with open(img_path1,"rb") as f:
            img1_data = f.read()

        with open(img_path2,"rb") as f:
            img2_data = f.read()

        rec_remain = rec_num

        ofst = int(rec_ofst / self.display_hex_num) * self.display_hex_num
        end_flag = [0,0]

        empty_str = ""
        for i in range(int(self.display_hex_num/2)):
            empty_str += "~~"
            empty_str += " "
        empty_str += "  "
        for i in range(int(self.display_hex_num/2)):
            empty_str += "~~"
            empty_str += " "

        print("\n           ", end='')
        for i in range(self.display_hex_num):
            if i == int(self.display_hex_num/2):
                print("", end='  ')
            print(str(i).rjust(2,'0'), end=' ')
        print("      ", end='')
        for i in range(self.display_hex_num):
            if i == int(self.display_hex_num/2):
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
            for i in range(ofst, ofst+self.display_hex_num, 1):
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
            for i in range(ofst, ofst+self.display_hex_num, 1):
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
                self.color_split_print(img1_data, img1_focus, ofst)
                print("     ", end='')
                self.color_split_print(img2_data, img2_focus, ofst)
                print("")

            if end_flag[0] and end_flag[1]:
                break

            ofst += self.display_hex_num
        
        print("-------------------------------------------------------------------------------------------------------------------")
        print("image1 size: ", hex(len(img1_data)).rjust(8, '0'))
        print("image2 size: ", hex(len(img2_data)).rjust(8, '0'))
