class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # cols = collections.defaultdict(set)
        # rows = collections.defaultdict(set)
        # boxes = collections.defaultdict(set)
        rows = [[0] * 9 for _ in range(9)]
        cols = [[0] * 9 for _ in range(9)]
        boxes = [[0] * 9 for _ in range(9)]
        for row in range(0, 9):
            for col in range(0, 9):
                if board[row][col] == ".":continue
                val = int(board[row][col]) - 1
                boxInd = 3 * (row // 3) + (col // 3)
                if rows[row][val] == 1 or cols[col][val] == 1 or boxes[boxInd][val] == 1:
                    return False
                
                cols[col][val] = 1
                rows[row][val] = 1
                boxes[boxInd][val] = 1
        return True