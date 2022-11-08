# HEXDUMPER
Hex file explore tool.

### Purpose:
    Create a tool for hex files explore.
    - STANDARD MODE: Given certain offset and numbers to display image.
    - SEARCH MODE: Given search key list of bytes to explore in 1 image. 
    - COMPARE MDOE: Given 2 images for comparing same/diff elements or even display all.

### First rlease date:
    2022.11.08

### Version:
- 1.0.0 - First commit - 2022/11/08
  - Feature: none
  - Bug: none

### Required:
- OS
  - Linux: support
  - Windows: support
- Enviroment
  - python(version requirement not sure yet!)

### Usage
- Help
  - **i1/i**:  Image1 path
  - **i2**:    Image2 path
  - **m**:     Selet mode.
          - [0] STANDARD_MODE
          - [1] SEARCH_MODE
          - [2] COMPARE_MODE
          note: Default is STANDARD_MODE
  - **k**:     Hex list in SEARCH_MODE\
        note: Only work in SEARCH_MODE
  - **s**:      Display offset\
        note: Only work in STANDARD_MODE
  - **n**:      Display numbers of bytes\
        note: Only work in STANDARD_MODE
  - **f**:      Force to print all element\
        note: Only work in SEARCH_MODE/COMPARE_MODE and only support in LINUX
  - **c**:      Choose sub mode\
        note: Only work in COMPARE_MODE, default 0\
          * COMPARE_MODE\
            - [0] no filter (default)\
            - [1] find different\
            - [2] find same

- **EX1. STANDARD MODE**
```
(base) mouchen@mouchen-System-Product-Name:~/Documents/PYTHON_DATA/PY_DATA/HEX_DUMPER/release/v1.0.0$ ./hexdumper -i ./demo/GT_SWB_PEX0.bin -s 5f0 -n 27
========================================================
* APP name:    HEX DUMPER
* APP auth:    Mouchen
* APP version: 1.0.0
* APP date:    2022.11.08
========================================================
<system> Config set:
         * mode:       STANDARD MODE
         * image:      ./demo/GT_SWB_PEX0.bin
         * ofset:      0x5f0
         * number:     27

           00 01 02 03 04 05 06 07   08 09 10 11 12 13 14 15 
------------------------------------------------------------
000005f0   1f 1f 1f 00 00 00 03 03   00 00 01 b0 00 00 00 00 
00000600   00 cc 00 00 83 00 00 0f   10 1c 00                
------------------------------------------------------------
image size:  0x14e790
```

  - **EX2. SEARCH MODE**
```
(base) mouchen@mouchen-System-Product-Name:~/Documents/PYTHON_DATA/PY_DATA/HEX_DUMPER/release/v1.0.0$ ./hexdumper -i ./demo/GT_SWB_PEX0.bin -m 1 -k 04 00 00 00 00 00 01 00 00 00 00 00 04 00 00 00 04 00 02
========================================================
* APP name:    HEX DUMPER
* APP auth:    Mouchen
* APP version: 1.0.0
* APP date:    2022.11.08
========================================================
<system> Config set:
         * mode:       SEARCH MODE
         * image:      ./demo/GT_SWB_PEX0.bin
         * search_lst: [4, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 4, 0, 0, 0, 4, 0, 2]

           00 01 02 03 04 05 06 07   08 09 10 11 12 13 14 15 
------------------------------------------------------------
00000000                                               04 00 
00000010   00 00 00 00 01 00 00 00   00 00 04 00 00 00 04 00 
00000020   02                                                
------------------------------------------------------------
image size:  0x14e790

           00 01 02 03 04 05 06 07   08 09 10 11 12 13 14 15 
------------------------------------------------------------
00040000                                               04 00 
00040010   00 00 00 00 01 00 00 00   00 00 04 00 00 00 04 00 
00040020   02                                                
------------------------------------------------------------
image size:  0x14e790

           00 01 02 03 04 05 06 07   08 09 10 11 12 13 14 15 
------------------------------------------------------------
00148810                                               04 00 
00148820   00 00 00 00 01 00 00 00   00 00 04 00 00 00 04 00 
00148830   02                                                
------------------------------------------------------------
image size:  0x14e790

(base) mouchen@mouchen-System-Product-Name:~/Documents/PYTHON_DATA/PY_DATA/HEX_DUMPER/release/v1.0.0$ ./hexdumper -i ./demo/GT_SWB_PEX0.bin -m 1 -k 04 00 00 00 00 00 01 00 00 00 00 00 04 00 00 00 04 00 02 -f
========================================================
* APP name:    HEX DUMPER
* APP auth:    Mouchen
* APP version: 1.0.0
* APP date:    2022.11.08
========================================================
<system> Config set:
         * mode:       SEARCH MODE
         * image:      ./demo/GT_SWB_PEX0.bin
         * search_lst: [4, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 4, 0, 0, 0, 4, 0, 2]

           00 01 02 03 04 05 06 07   08 09 10 11 12 13 14 15 
------------------------------------------------------------
00000000   ef be ad de 01 00 0c 00   00 00 00 00 00 00 04 00 
00000010   00 00 00 00 01 00 00 00   00 00 04 00 00 00 04 00 
00000020   02 00 00 00 00 00 18 00   00 00 08 00 03 00 00 00 
------------------------------------------------------------
image size:  0x14e790

           00 01 02 03 04 05 06 07   08 09 10 11 12 13 14 15 
------------------------------------------------------------
00040000   ef be ad de 01 00 0c 00   00 00 00 00 00 00 04 00 
00040010   00 00 00 00 01 00 00 00   00 00 04 00 00 00 04 00 
00040020   02 00 00 00 00 00 18 00   00 00 08 00 03 00 00 00 
------------------------------------------------------------
image size:  0x14e790

           00 01 02 03 04 05 06 07   08 09 10 11 12 13 14 15 
------------------------------------------------------------
00148810   ff ff ff ff 01 00 0c 00   00 00 00 00 00 00 04 00 
00148820   00 00 00 00 01 00 00 00   00 00 04 00 00 00 04 00 
00148830   02 00 00 00 00 00 18 00   00 00 08 00 03 00 00 00 
------------------------------------------------------------
image size:  0x14e790
```

  - **EX3. COMPARE MODE**
           --> python img_comb.py --> choose mode[1] to use cfg-offset mode
```
(base) mouchen@mouchen-System-Product-Name:~/Documents/PYTHON_DATA/PY_DATA/HEX_DUMPER/release/v1.0.0$ ./hexdumper -i1 ./demo/GT_SWB_PEX0.bin -i2 ./demo/GT_SWB_PEX1.bin -m 2 -c 1
========================================================
* APP name:    HEX DUMPER
* APP auth:    Mouchen
* APP version: 1.0.0
* APP date:    2022.11.08
========================================================
<system> Config set:
         * mode:       COMPARE MODE
         * image1:     ./demo/GT_SWB_PEX0.bin
         * image2:     ./demo/GT_SWB_PEX1.bin

           00 01 02 03 04 05 06 07   08 09 10 11 12 13 14 15       00 01 02 03 04 05 06 07   08 09 10 11 12 13 14 15 
-------------------------------------------------------------------------------------------------------------------
000005f0   ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~   00 ~~ ~~ ~~ ~~ ~~ ~~ ~~      ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~   01 ~~ ~~ ~~ ~~ ~~ ~~ ~~ 
00000600   00 ~~ ~~ ~~ ~~ ~~ ~~ ~~   ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~      01 ~~ ~~ ~~ ~~ ~~ ~~ ~~   ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ 
000007d0   60 ~~ ~~ ~~ ~~ ~~ ~~ ~~   ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~      61 ~~ ~~ ~~ ~~ ~~ ~~ ~~   ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ 
00000c20   cf ~~ ~~ ~~ ~~ ~~ ~~ ~~   ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~      cc ~~ ~~ ~~ ~~ ~~ ~~ ~~   ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ 
000405f0   ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~   00 ~~ ~~ ~~ ~~ ~~ ~~ ~~      ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~   01 ~~ ~~ ~~ ~~ ~~ ~~ ~~ 
00040600   00 ~~ ~~ ~~ ~~ ~~ ~~ ~~   ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~      01 ~~ ~~ ~~ ~~ ~~ ~~ ~~   ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ 
000407d0   60 ~~ ~~ ~~ ~~ ~~ ~~ ~~   ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~      61 ~~ ~~ ~~ ~~ ~~ ~~ ~~   ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ 
00040c20   cf ~~ ~~ ~~ ~~ ~~ ~~ ~~   ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~      cc ~~ ~~ ~~ ~~ ~~ ~~ ~~   ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ 
0014c7b0   ~~ ~~ ~~ ~~ 00 ~~ ~~ ~~   ~~ ~~ ~~ ~~ 00 ~~ ~~ ~~      ~~ ~~ ~~ ~~ 01 ~~ ~~ ~~   ~~ ~~ ~~ ~~ 01 ~~ ~~ ~~ 
0014c980   ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~   ~~ ~~ ~~ ~~ 60 ~~ ~~ ~~      ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~   ~~ ~~ ~~ ~~ 61 ~~ ~~ ~~ 
0014cdd0   ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~   ~~ ~~ ~~ ~~ cf ~~ ~~ ~~      ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~   ~~ ~~ ~~ ~~ cc ~~ ~~ ~~ 
0014ce10   ~~ ~~ ~~ ~~ 47 04 ~~ ad   ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~      ~~ ~~ ~~ ~~ 6f 30 ~~ ac   ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ 
0014cee0   ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~   ~~ 20 ~~ ~~ ~~ ~~ ~~ ~~      ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~   ~~ 21 ~~ ~~ ~~ ~~ ~~ ~~ 
0014cef0   ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~   ~~ ~~ ~~ ~~ ~~ ~~ ~~ 30      ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~   ~~ ~~ ~~ ~~ ~~ ~~ ~~ 31 
0014d830   ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~   ~~ ~~ ~~ ~~ ~~ 90 ~~ ~~      ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~   ~~ ~~ ~~ ~~ ~~ 67 ~~ ~~ 
0014d860   ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~   ~~ ~~ ~~ ~~ 00 ~~ ~~ ~~      ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~   ~~ ~~ ~~ ~~ 01 ~~ ~~ ~~ 
0014d880   ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~   15 ~~ ~~ ~~ ~~ ~~ ~~ ~~      ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~   17 ~~ ~~ ~~ ~~ ~~ ~~ ~~ 
0014d8a0   14 ~~ ~~ ~~ ~~ ~~ ~~ ~~   ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~      16 ~~ ~~ ~~ ~~ ~~ ~~ ~~   ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ 
0014d8b0   ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~   21 ~~ ~~ ~~ ~~ ~~ ~~ ~~      ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~   25 ~~ ~~ ~~ ~~ ~~ ~~ ~~ 
0014d8d0   20 ~~ ~~ ~~ ~~ ~~ ~~ ~~   ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~      24 ~~ ~~ ~~ ~~ ~~ ~~ ~~   ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ 
0014d8e0   ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~   1f ~~ ~~ ~~ ~~ ~~ ~~ ~~      ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~   23 ~~ ~~ ~~ ~~ ~~ ~~ ~~ 
0014d900   1e ~~ ~~ ~~ ~~ ~~ ~~ ~~   ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~      22 ~~ ~~ ~~ ~~ ~~ ~~ ~~   ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ 
0014d910   ~~ ~~ ~~ ~~ ~~ 00 ~~ ~~   3b ~~ ~~ ~~ ~~ ~~ ~~ ~~      ~~ ~~ ~~ ~~ ~~ ff ~~ ~~   00 ~~ ~~ ~~ ~~ ~~ ~~ ~~ 
0014d930   34 ~~ ~~ ~~ ~~ ~~ ~~ ~~   ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~      35 ~~ ~~ ~~ ~~ ~~ ~~ ~~   ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ 
0014d970   ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~   36 ~~ ~~ ~~ ~~ ~~ ~~ ~~      ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~   33 ~~ ~~ ~~ ~~ ~~ ~~ ~~ 
0014d9a0   ~~ ~~ ~~ ~~ ~~ 29 ~~ ~~   ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~      ~~ ~~ ~~ ~~ ~~ 27 ~~ ~~   ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ 
0014d9e0   ~~ ~~ ~~ ~~ ~~ 05 ~~ ~~   ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~      ~~ ~~ ~~ ~~ ~~ 04 ~~ ~~   ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ 
0014d9f0   ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~   ~~ ~~ 01 ~~ ~~ ~~ ~~ ~~      ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~   ~~ ~~ 00 ~~ ~~ ~~ ~~ ~~ 
-------------------------------------------------------------------------------------------------------------------
image1 size:  0x14e790
image2 size:  0x14e790

(base) mouchen@mouchen-System-Product-Name:~/Documents/PYTHON_DATA/PY_DATA/HEX_DUMPER/release/v1.0.0$ ./hexdumper -i1 ./demo/GT_SWB_PEX0.bin -i2 ./demo/GT_SWB_PEX1.bin -m 2 -c 1 -f
========================================================
* APP name:    HEX DUMPER
* APP auth:    Mouchen
* APP version: 1.0.0
* APP date:    2022.11.08
========================================================
<system> Config set:
         * mode:       COMPARE MODE
         * image1:     ./demo/GT_SWB_PEX0.bin
         * image2:     ./demo/GT_SWB_PEX1.bin

           00 01 02 03 04 05 06 07   08 09 10 11 12 13 14 15       00 01 02 03 04 05 06 07   08 09 10 11 12 13 14 15 
-------------------------------------------------------------------------------------------------------------------
000005f0   1f 1f 1f 00 00 00 03 03   00 00 01 b0 00 00 00 00      1f 1f 1f 00 00 00 03 03   01 00 01 b0 00 00 00 00 
00000600   00 cc 00 00 83 00 00 0f   10 1c 00 04 66 03 00 1f      01 cc 00 00 83 00 00 0f   10 1c 00 04 66 03 00 1f 
000007d0   60 00 00 00 a5 00 00 0f   09 09 09 09 09 09 09 09      61 00 00 00 a5 00 00 0f   09 09 09 09 09 09 09 09 
00000c20   cf 00 00 00 00 00 00 00   00 00 00 00 ff ff ff ff      cc 00 00 00 00 00 00 00   00 00 00 00 ff ff ff ff 
000405f0   1f 1f 1f 00 00 00 03 03   00 00 01 b0 00 00 00 00      1f 1f 1f 00 00 00 03 03   01 00 01 b0 00 00 00 00 
00040600   00 cc 00 00 83 00 00 0f   10 1c 00 04 66 03 00 1f      01 cc 00 00 83 00 00 0f   10 1c 00 04 66 03 00 1f 
000407d0   60 00 00 00 a5 00 00 0f   09 09 09 09 09 09 09 09      61 00 00 00 a5 00 00 0f   09 09 09 09 09 09 09 09 
00040c20   cf 00 00 00 00 00 00 00   00 00 00 00 ff ff ff ff      cc 00 00 00 00 00 00 00   00 00 00 00 ff ff ff ff 
0014c7b0   00 00 03 03 00 00 01 b0   00 00 00 00 00 cc 00 00      00 00 03 03 01 00 01 b0   00 00 00 00 01 cc 00 00 
0014c980   99 00 00 1f 01 00 00 00   92 03 00 1f 60 00 00 00      99 00 00 1f 01 00 00 00   92 03 00 1f 61 00 00 00 
0014cdd0   5d 07 10 02 c8 2b 00 7b   64 00 64 00 cf 00 00 00      5d 07 10 02 c8 2b 00 7b   64 00 64 00 cc 00 00 00 
0014ce10   00 ff ff ff 47 04 5a ad   00 00 00 00 00 00 00 00      00 ff ff ff 6f 30 5a ac   00 00 00 00 00 00 00 00 
0014cee0   20 20 20 20 20 20 20 20   f9 20 ff ff 08 01 01 09      20 20 20 20 20 20 20 20   f9 21 ff ff 08 01 01 09 
0014cef0   00 41 01 29 22 47 54 2d   53 57 42 2d 50 45 58 30      00 41 01 29 22 47 54 2d   53 57 42 2d 50 45 58 31 
0014d830   00 00 00 00 00 00 00 00   00 00 00 00 f9 90 ff ff      00 00 00 00 00 00 00 00   00 00 00 00 f9 67 ff ff 
0014d860   00 03 00 04 00 04 00 02   00 00 9b 1d 00 cc 00 00      00 03 00 04 00 04 00 02   00 00 9b 1d 01 cc 00 00 
0014d880   00 00 00 00 00 00 00 00   15 00 00 00 00 00 00 00      00 00 00 00 00 00 00 00   17 00 00 00 00 00 00 00 
0014d8a0   14 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00      16 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00 
0014d8b0   00 00 00 00 20 00 00 00   21 00 00 00 00 00 00 00      00 00 00 00 20 00 00 00   25 00 00 00 00 00 00 00 
0014d8d0   20 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00      24 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00 
0014d8e0   00 00 00 00 28 00 00 00   1f 00 00 00 00 00 00 00      00 00 00 00 28 00 00 00   23 00 00 00 00 00 00 00 
0014d900   1e 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00      22 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00 
0014d910   00 00 00 00 30 00 00 00   3b 00 00 00 00 00 00 00      00 00 00 00 30 ff 00 00   00 00 00 00 00 00 00 00 
0014d930   34 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00      35 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00 
0014d970   00 00 00 00 70 00 00 00   36 00 00 00 00 00 00 00      00 00 00 00 70 00 00 00   33 00 00 00 00 00 00 00 
0014d9a0   00 00 00 00 f9 29 ff ff   74 00 0f e0 50 04 44 00      00 00 00 00 f9 27 ff ff   74 00 0f e0 50 04 44 00 
0014d9e0   00 00 00 00 60 05 44 00   00 00 00 00 19 00 00 19      00 00 00 00 60 04 44 00   00 00 00 00 19 00 00 19 
0014d9f0   ff ff ff 00 00 00 01 00   00 11 01 00 00 00 00 00      ff ff ff 00 00 00 01 00   00 11 00 00 00 00 00 00 
-------------------------------------------------------------------------------------------------------------------
image1 size:  0x14e790
image2 size:  0x14e790
```

### Note
- 1: Force display with color only supported in Linux. 
