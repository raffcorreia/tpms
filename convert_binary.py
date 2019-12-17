#!/usr/bin/env python

#
# 2019 - Rafael Correia
#
# This script was created to convert lines with hex values separated by space into its equivalent binary values
# 
#  
# 
# 


import sys
import string

def main(filePath):
    l = 0
    with open(filePath) as f:
        for line in f:
            if 'str' in line:
                break
            if line.strip() != '':
                l += 1
                convertLine(*line.split(' '))
    return l

def convertLine(*strHex):
    binValue = ''
    for value in strHex:
        if all(c in string.hexdigits for c in value) and len(value) > 0:
            binValue += bin(int(value, 16))[2:].zfill(8)
    binList.append(binValue)
    # print(binValue)
    

binList     = []

if __name__ == "__main__":
    lineCount = main("~/Downloads/sdr/TPMS/samples/selected.txt")
    print(binList)
    print("Found {} unique and non empty lines out of {} original non empty lines.".format(len(binList), lineCount))

# for arg in sys.argv[1:]:
#     print arg