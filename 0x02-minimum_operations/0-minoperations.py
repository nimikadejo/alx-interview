#!/usr/bin/python3
''' Module for function '''


def minOperations(n):
    '''
    Deternmines minimum number of operations to get
    1 to n with copy all and paste
    '''
    content = 1
    ops = 0
    copy = 0

    if n < 1:
        return 0
    if n % 10 == 0 and n > 20:
        while content < n:
            if n % content == 0:
                copy += content
                ops += 2  # copy and paste
            else:
                copy += content
                ops += 1  # paste
        content += copy
    if (n < 20):
        if n % 2 == 0:
            ops = ((n/2) - 1) + 3
        if n % 3 == 0:
            ops = ((n/3) - 1) + 4
    else:
        ops = n
    return ops
