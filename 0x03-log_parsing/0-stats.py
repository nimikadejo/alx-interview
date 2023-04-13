#!/usr/bin/python3
'''
A script that reads stdin line by line and computes metrics
'''


import sys


def print__http_status_logs(dic, total_size):
    """ Prints std line """
    print("File size: {:d}".format(total_size))
    for i in sorted(dic.keys()):
        if dic[i] != 0:
            print("{}: {:d}".format(i, dic[i]))


choice = {'200': 0, '301': 0, '400': 0, '401': 0,
          '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
n = 0

try:
    for line in sys.stdin:
        line_list = line.split(" ")
        if len(line_list) > 4:
            code = line_list[-2]
            size = int(line_list[-1])
            if code in choice.keys():
                choice[code] += 1
            total_size += size
            n += 1

except Exception as err:
    pass

finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted(choice.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
