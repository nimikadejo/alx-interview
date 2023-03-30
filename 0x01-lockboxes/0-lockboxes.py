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
  currentBox = [0]  #a list of current box opened

  while currentBox:
    index = currentBox.pop(0) #call top of stack
    for num in boxes[index]:
      if not openedBox[num] and num < allBoxes:
        opened[num] = True
        currentBox.append(num)
  return all(opened)

