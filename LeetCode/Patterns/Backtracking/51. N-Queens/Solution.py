class Solution:
    def isSafe(self, row, col, n, board):
        temp_col = col
        temp_row = row
        
        while col >= 0 and row >= 0:
            if board[row][col] == 'Q':return False
            row -= 1
            col -= 1
        
        col = temp_col
        row = temp_row
        while col >= 0:
            if board[row][col] == 'Q':return False
            col -= 1
        col = temp_col
        
        
        while row < n and col >= 0:
            if board[row][col] == 'Q':return False
            row += 1
            col -= 1
        return True
    
    def placeQueen(self, n, col, leftRow, lowerDiagonal, upperDiagonal, board, ans):
        if col == n:
            ans.append(board[:])
            return 
        for row in range(0, n):
            if leftRow[row] == 0 and lowerDiagonal[row + col] == 0 \
            and upperDiagonal[n - 1 + col - row] == 0:
                board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                leftRow[row] = 1 
                lowerDiagonal[row + col] = 1
                upperDiagonal[n - 1 + col - row] = 1
                self.placeQueen(n, col + 1, leftRow, lowerDiagonal, upperDiagonal, board, ans)
                board[row] = board[row][:col] + '.' + board[row][col+1:]
                leftRow[row] = 0 
                lowerDiagonal[row + col] = 0
                upperDiagonal[n - 1 + col - row] = 0

    def solveNQueens(self, n: int) -> list[list[str]]:
        ans = []
        # board = ["." * n for _ in range(n)]
        leftRow = [0]*n
        lowerDiagonal = [0]*(2*n - 1)
        upperDiagonal = [0]*(2*n - 1)
        self.placeQueen(n, 0, leftRow, lowerDiagonal, upperDiagonal, ["."*n]*n, ans)
        
        return ans

