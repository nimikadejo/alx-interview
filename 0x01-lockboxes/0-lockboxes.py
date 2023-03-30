#!/usr/bin/python3
''' Module to return function'''


def canUnlockAll(boxes):
    '''
    Args:
    boxes(list): list of lists
    Returns:
    Boolean
    '''
    allBoxes = len(boxes)
    openedBox = [False] * allBoxes
    openedBox[0] = True
    currentBox = [0]

    while currentBox:
        index = currentBox.pop(0)
        for num in boxes[index]:
            if not openedBox[num] and num < allBoxes and num >= 0:
                opened[num] = True
                currentBox.append(num)
    return all(opened)
