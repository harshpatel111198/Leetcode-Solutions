class Solution:
    def isValid(self, board, row, col, c):
        for j in range(0,9):
            if board[j][col] == c:
                return False
            if board[row][j] == c:
                return False
            elif board[3 * (row // 3) + j // 3][3 * (col//3) + j % 3] == c:
                return False
        return True
    def placeNumber(self, board):

        for row in range(0, 9):
            for col in range(0, 9):
                if board[row][col] == ".":
                    for c in range(0, 9):
                        if self.isValid(board, row, col, str(c + 1)):
                            board[row][col] = str(c + 1)
                            if self.placeNumber(board):
                                return True
                            else:
                                board[row][col] = "."
                    return False
        return True

            
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.placeNumber(board)