#!/usr/bin/env python

import sys
from math import floor

def val(comp, app):
    return sum([ord(app[i]) for i in range(comp)])


def main(password=None):
        # pass._0_8_ = 0x48426a50434a7a77;
        # pass._8_8_ = 0x6162486b41487342;
        # pass._16_8_ = 0x7a6c666459686d7a;
        # pass._24_8_ = 0x455550706168644c;

    if password == None:
        passwordChunks = ["0x48426a50434a7a77", "0x6162486b41487342", "0x7a6c666459686d7a", "0x455550706168644c"]
        
        password = ""
        for chunk in passwordChunks:
            bytes_object = bytes.fromhex(chunk[2:])
            password += bytes_object.decode("ASCII")

    pass_length = len(password)
    value = val(pass_length, password)

    meanValue = value / pass_length
    full = value // pass_length
    residue = value % pass_length

    print(f'Password: {password}; Length: {pass_length}')
    print(f'Val(): {value} = {full}*{pass_length} + {residue}')
    # print(f'Mean value for each char: {meanValue}')
    
    char = ord('a')
    charNum = value // char
    charRes = value % char


    validPassword = ""
    if charRes == 0:
        validPassword = chr(char)*charNum
    else:
        validPassword = chr(char)*(charNum) + chr(charRes)


    print(f'Valid password: {validPassword}; Length: {len(validPassword)}')
    print(f'Val(): {value} = {full}*{pass_length} + {residue}')

    

if __name__ == "__main__":
    args = sys.argv

    if len(args) == 1:
        main()
    else:
       main(args[1])
