class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        boxes = collections.defaultdict(set)
        for row in range(0, 9):
            for col in range(0, 9):
                val = board[row][col] 
                if val == ".":continue
                if val in rows[row] or val in cols[col] or val in boxes[(row//3, col//3)]:
                    return False
                
                cols[col].add(board[row][col])
                rows[row].add(board[row][col])
                

                
                boxes[(row//3, col//3)].add(board[row][col])
        return True