#!/usr/bin/python3
''' Module for function '''


def minOperations(n):
    '''
    Deternmines minimum number of operations to get
    1 to n with copy all and paste
    '''
    if n < 1:
        return 0

    content = 1
    copy = 0
    ops = 0

    while content < n:
        if n % content == 0:
            copy = content
            ops += 2
        else:
            copy += content
            ops += 1
        content += copy

    if content == n:
        return ops
    else:
        return 0
