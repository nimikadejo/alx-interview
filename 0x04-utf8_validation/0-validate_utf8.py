#!/usr/bin/python3
'''
A script that determines if a given data set represents a valid UTF-8 encoding.
'''


def validUTF8(data):
    #  Initialize the number of bytes left to read for a character
    bytes_left = 0

    #  Loop through every byte in input data set
    for b in data:
        #  If no bytes left to read,
        #  determine the number of bytes for next character
        if bytes_left == 0:
            if b >> 5 == 0b110 or b >> 5 == 0b1110:
                bytes_left = 1
            elif b >> 4 == 0b1110:
                bytes_left = 2
            elif b >> 3 == 0b11110:
                bytes_left = 3
            elif b >> 7 == 0b1:
                return False
        else:
            if b >> 6 != 0b10:
                return False
            bytes_left -= 1

    if bytes_left > 0:
        return False

    return True
