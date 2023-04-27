#!/usr/bin/python3
'''
A script that solves the N queens problem.
'''


import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if n < 4:
        print('N must be at least 4')
        exit(1)

    solutions = []
    placed_queens = []  # coordinates format [row, column]
    stop = False
    rows = 0
    c = 0

    # iterate thru rows
    while rows < n:
        goback = False
        # iterate thru columns
        while c < n:
            # check is current column is safe
            safe = True
            for cord in placed_queens:
                col = cord[1]
                if (col == c or col + (rows-cord[0]) == c
                        or col - (rows-cord[0]) == c):
                    safe = False
                    break

            if not safe:
                if c == n - 1:
                    goback = True
                    break
                c += 1
                continue

            # place queen
            cords = [rows, c]
            placed_queens.append(cords)
            # if last row, append solution and reset all to last unfinished row
            # and last safe column in that row
            if rows == n - 1:
                solutions.append(placed_queens[:])
                for cord in placed_queens:
                    if cord[1] < n - 1:
                        rows = cord[0]
                        c = cord[1]
                for i in range(n - rows):
                    placed_queens.pop()
                if rows == n - 1 and c == n - 1:
                    placed_queens = []
                    stop = True
                rows -= 1
                c += 1
            else:
                c = 0
            break
        if stop:
            break
        # on fail: go back to previous row
        # and continue from last safe column + 1
        if goback:
            rows -= 1
            while rows >= 0:
                c = placed_queens[rows][1] + 1
                del placed_queens[rows]  # delete previous queen coordinates
                if c < n:
                    break
                rows -= 1
            if rows < 0:
                break
            continue
        rows += 1

    for idx, val in enumerate(solutions):
        if idx == len(solutions) - 1:
            print(val, end='')
        else:
            print(val)
