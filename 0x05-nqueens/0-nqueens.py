#!/usr/bin/python3
'''
A script that solves the N queens problem.
'''


import sys

# Check if N is a valid integer
try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

# Check if N is greater than or equal to 4
if N < 4:
    print("N must be at least 4")
    sys.exit(1)


# Function to check if a position is safe for a queen
def isSafe(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


# Recursive function to solve N Queens problem
def solveNQueens(board, col):
    # Base case: If all queens are placed, print the solution
    if col == N:
        for i in range(N):
            for j in range(N):
                print(board[i][j], end=' ')
            print()
        print()
        return True

    # Initialize the flag to keep track of safe position for queen
    res = False

    # Check every row in this column
    for i in range(N):
        if isSafe(board, i, col):
            # Place the queen
            board[i][col] = 1

            # Check if it leads to a solution
            res = solveNQueens(board, col+1) or res

            # Backtrack and remove the queen from this position
            board[i][col] = 0

    return res


# Initialize the board with 0s
board = [[0 for x in range(N)] for y in range(N)]

# Call the recursive function to solve the problem
if not solveNQueens(board, 0):
    print("No solution exists")
