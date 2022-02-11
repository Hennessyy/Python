#!/usr/bin/python3

import sys

inp_one = sys.argv[1]
inp_two = sys.argv[2]

print(bin(int(inp_one))[2:].rjust(4, "0"))
print(bin(int(inp_two))[2:].rjust(4, "0"))

# bitwise and

if inp_one.isdigit() and inp_two.isdigit():
    print(bin(int(inp_one) & int(inp_two))[2:].rjust(4, "0"))


#bitwise or

if inp_one.isdigit() and inp_two.isdigit():
    print(bin(int(inp_one) | int(inp_two))[2:].rjust(4, "0"))

#bit shift

print(bin(int(inp_one) << 2 )[2:].rjust(4, "0"))