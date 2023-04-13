#!/usr/bin/python3
'''
A script that reads stdin line by line and computes metrics
'''


import sys

choice = {'200': 0, '301': 0, '400': 0, '401': 0,
          '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
n = 0

try:
    for line in sys.stdin:
        line_list = line.split()
        if len(line_list) > 4:
            code = line_list[-2]
            size = int(line_list[-1])
            if code in choice:
                choice[code] += 1
            total_size += size
            n += 1

        if n == 10:
            n = 0
            print('File size: {}'.format(total_size))
            for key, value in sorted(choice.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except KeyboardInterrupt:
    pass

finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted(choice.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
