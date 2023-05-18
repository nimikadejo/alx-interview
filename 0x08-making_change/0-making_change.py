#!/usr/bin/python3
"""making change"""


def makeChange(coins, total):
    '''determine the fewest number of coins needed to meet a given amount
    '''
    if total < 0:
        return 0
    arr = [0] + [float("inf")] * (total)

    for num in coins:
        for x in range(num, total + 1):
            arr[x] = min(arr[x], arr[x - num] + 1)
    return arr[total] if arr[total] != float('inf') else -1
