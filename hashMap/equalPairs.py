#!/usr/bin/env python3

# Equal Row and Column Pairs

# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.
# A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

grid = [[3,2,1],[1,7,6],[2,7,7]]
# Output should be 1
def equalPairs(grid) -> int:
    numberOfRows = numberOfCols = len(grid)
    rows = {}
    count = 0
    for r in range(numberOfRows): # for every row in the grid
        # row is the key of rows dictionary
        row = tuple(grid[r]) # so [3,2,1] (our first row) is converted to (3,2,1)
        # set the value of each key in rows dict
        rows[row] = 1 + rows.get(row, 0) 

    for c in range(numberOfCols):
        col = tuple(grid[i][c] for i in range(numberOfRows)) 
        # check if col exists as a key in the dictionary rows
        count += rows.get(col, 0)
    
    return count



# My Note: 
# The get() method returns the value of the item with the specified key.

