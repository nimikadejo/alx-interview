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
    def isPrime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Function to find the next prime number in the set
    def findNextPrime(nums):
        for num in nums:
            if isPrime(num):
                return num
        return None

    # Function to remove a number and its multiples from the set
    def removeMultiples(nums, prime):
        return [num for num in nums if num % prime != 0]

    # Function to determine the winner of a single round
    def playRound(nums):
        while True:
            prime = findNextPrime(nums)
            if prime is None:
                return "Ben"
            nums = removeMultiples(nums, prime)
            if len(nums) == 0:
                return "Maria"

    # Play x rounds and keep track of the winners
    winners = []
    for n in nums:
        winner = playRound(list(range(1, n + 1)))
        winners.append(winner)

    # Count the number of wins for each player
    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    # Determine the player with the most wins
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
