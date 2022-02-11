#!/usr/bin/python3

import sys

inp = sys.argv[1]

if inp.isdigit():
    print(bin(int(inp))[2:].rjust(4, "0"))
else:
    print("Invalid argument passed - must be an integer") 