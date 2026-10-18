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
    
    def placeQueen(self, n, col, board, ans):
        if col == n:
            ans.append(board[:])
            return 
        for row in range(0, n):
            if self.isSafe(row, col, n, board):
                board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                self.placeQueen(n, col + 1, board, ans)
                board[row] = board[row][:col] + '.' + board[row][col+1:]

    def solveNQueens(self, n: int) -> list[list[str]]:
        ans = []
        # board = ["." * n for _ in range(n)]

        self.placeQueen(n, 0, ["."*n]*n, ans)
        
        return ans

