#!/usr/bin/python3
''' Module to return function'''


def canUnlockAll(boxes):
    '''
    Determines if all boxes can be opened.
    Returns True if all boxes can be opened, else returns False
    '''
    allBoxes = len(boxes)
    openedBox = [False] * allBoxes
    openedBox[0] = True
    currentBox = [0]  # opened box

    while currentBox:
        index = currentBox.pop(0)  # take the key at the top of the stack
        for num in boxes[index]:
            if num < allBoxes and num >= 0 and not openedBox[num]:
                openedBox[num] = True
                currentBox.append(num)  # add recently opened box to index
    return all(openedBox)
