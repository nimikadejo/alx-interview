#!/usr/bin/python3
'''
A script that reads stdin line by line and computes metrics
'''


import sys


def print_http_status_logs(add, size):
    """ Prints std line """
    print("File size: {:d}".format(size))
    for i in sorted(add.keys()):
        if add[i] != 0:
            print("{}: {:d}".format(i, add[i]))


http_status_array = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

count = 0
size = 0

try:
    for ln in sys.stdin:
        if count != 0 and count % 10 == 0:
            print_http_status_logs(http_status_array, size)
        status_list = ln.split()
        count += 1
        try:
            size += int(status_list[-1])
        except ValueError:
            pass
        try:
            if status_list[-2] in http_status_array:
                http_status_array[status_list[-2]] += 1
        except IndexError:
            pass
    print_http_status_logs(http_status_array, size)
except KeyboardInterrupt:
    print_http_status_logs(http_status_array, size)
    raise KeyboardInterrupt
