#!/usr/bin/python3
''' Module to return function'''


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    Returns True if all boxes can be opened, else returns False.
    """
    n = len(boxes)
    unlocked = [False] * n  # Keeps track of whether each box is unlocked
    unlocked[0] = True  # The first box is already unlocked
    queue = [0]  # Start with the first box
    while queue:
        box = queue.pop(0)
        for key in boxes[box]:
            if key >= 0 and key < n and not unlocked[key]:
                # The key is valid and it unlocks a new box
                unlocked[key] = True
                queue.append(key)
    return all(unlocked)
