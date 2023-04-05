#!/usr/bin/python3
''' Module for function '''


def minOperations(n):
    '''
    Determines minimum number of operations to get
    1 to n with copy all and paste
    '''
    ops = 0
    content = 1
    copy = 0

    if n > 1:
        while content < n:
            if n % content == 0:
                copy = content
                content += copy
                ops += 2  # copy and paste
            else:
                content += copy
                ops += 1  # paste
    else:
        ops = 0

    return ops
