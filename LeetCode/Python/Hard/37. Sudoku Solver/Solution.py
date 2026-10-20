class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 1. Use sets to track what numbers already exist in each row, col, and 3x3 box
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []
        
        # 2. Single scan to initialize our sets and collect all empty coordinates
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != ".":
                    rows[r].add(val)
                    cols[c].add(val)
                    box_idx = (r // 3) * 3 + (c // 3)
                    boxes[box_idx].add(val)
                else:
                    empty_cells.append((r, c))
                    
        # 3. Direct index-based backtracking function
        def backtrack(index: int) -> bool:
            # If we've filled all empty cells, the puzzle is solved!
            if index == len(empty_cells):
                return True
                
            r, c = empty_cells[index]
            box_idx = (r // 3) * 3 + (c // 3)
            
            # Try placing digits '1' through '9'
            for val in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
                # O(1) Instant Lookup Check
                if val not in rows[r] and val not in cols[c] and val not in boxes[box_idx]:
                    # Make a choice
                    board[r][c] = val
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[box_idx].add(val)
                    
                    # Recursively move directly to the next empty cell
                    if backtrack(index + 1):
                        return True
                        
                    # Backtrack (Undo choice)
                    board[r][c] = "."
                    rows[r].remove(val)
                    cols[c].remove(val)
                    boxes[box_idx].remove(val)
                    
            return False

        # Start the backtracking at the first empty cell index
        backtrack(0)
