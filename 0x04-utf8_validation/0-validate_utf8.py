#!/usr/bin/python3
'''
A script that determines if a given data set represents a valid UTF-8 encoding.
'''


def valid_utf8(utf8_data):
    #  Initialize the number of bytes left to read for a character
    bytes_left = 0

    #  Loop through every byte in input data set
    for byte in utf8_data:
        #  If no bytes left to read,
        #  determine the number of bytes for next character
        if bytes_left == 0:
            if byte >> 5 == 0b110:
                bytes_left = 1
            elif byte >> 4 == 0b1110:
                bytes_left = 2
            elif byte >> 3 == 0b11110:
                bytes_left = 3
            elif byte >> 7 == 1:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            bytes_left -= 1

    if bytes_left > 0:
        return False

    return True
