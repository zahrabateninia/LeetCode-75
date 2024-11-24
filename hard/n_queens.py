# Brute force approach - we use backtracking
# Every queen should be placed on a separate row, column, positive and negative diagonal, so they can never attack each other 
# The hard part is diagonal 
# watch https://www.youtube.com/watch?v=Ph95IHmRp5M for clarification

# (n: int) -> List[List[str]]
def solveNQueens(n):
    col = set()
    posDiag = set() # it's determined by col index + row index
    negDiag = set() # row - col 

    res = [] # all the n-queens solutions
    # create a n * n array initially filled with . (meaning no queens are placed yet)
    board = [["."]* n for i in range(n)]

    # start row by row (each row can obviously have one queen in it)
    def backtrack(row):
        # we initially start from row 0 and we go until we get to row n
        # base case: we are completed all the rows 

        # copy each row in board and join each row together
        copy = ["".join(row) for row in board]
        res.append(copy)