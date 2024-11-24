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
        return

        # if we did not reach the base case

        # we are not allowed to use this column and row condition:
        for c in range(n):
            if c in col or(c+r) in posDiag or (r-c) in negDiag:
                continue
            # update
            col.add(c)
            posDiag.add(c+r)
            negDiag.add(r-c)
            board[r][c]= "Q" # place the queen not . anymore


            # go to the next row
            backtrack(r+1)

            # undo the things, that's what backtracking means
            col.remove(c)
            posDiag.remove(c+r)
            negDiag.remove(r-c)
            board[r][c]= "." 
            
        backtrack(0)
        return res