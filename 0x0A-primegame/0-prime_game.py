#!/usr/bin/python3

"""
Module to determine the winner of each game
"""


def isWinner(x, nums):
    """
    Determines who the winner of each game is

    Args:
        x (int): number of rounds
        nums (int): an array of n
    """
    if x < 1 or not nums:
        return None
    maria_wins, ben_wins = 0, 0

    max_n = max(nums)
    primes = [True for _ in range(1, max_n + 1, 1)]
    primes[0] = False

    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, max_n + 1, i):
            primes[j - 1] = False

    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        ben_wins += primes_count % 2 == 0
        maria_wins += primes_count % 2 == 1
    if maria_wins == ben_wins:
        return None
    return 'Maria' if maria_wins > ben_wins else 'Ben'
