class Solution:
    # def isValid(self, board, row, col, c):
    #     for j in range(0,9):
    #         if board[j][col] == c:
    #             return False
    #         if board[row][j] == c:
    #             return False
    #         if board[3 * (row // 3) + j // 3][3 * (col//3) + j % 3] == c:
    #             return False
    #     return True
    def placeNumber(self, board):

        for row in range(0, 9):
            for col in range(0, 9):
                if board[row][col] == ".":
                    box_row_start = 3 * (row // 3)
                    box_col_start = 3 * (col // 3)
                    for c in ("1","2","3","4","5","6","7","8","9"):
                        is_valid = True
                        for j in range(0,9):
                            if (board[row][j] == c or 
                            board[j][col] == c or 
                            board[box_row_start + (j // 3)][box_col_start + (j % 3)] == c):
                                is_valid = False
                                break


                        if is_valid:
                            board[row][col] = c
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