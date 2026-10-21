class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = set()
        dirc = [[0,1],[1,0],[0,-1],[-1,0]]

        def dfs(r,c,p):
            if p == len(word):
                return True
            if r not in range(m) or c not in range(n) or board[r][c] != word[p] or (r,c) in visited:
                return False
            visited.add((r,c))
            result = (dfs(r+1,c,p+1) or
                        dfs(r-1,c,p+1) or
                        dfs(r,c+1,p+1) or 
                        dfs(r,c-1,p+1))
            visited.remove((r,c))
            return result
        for i in range(m):
            for j in range(n):

                if dfs(i,j,0):
                    return True
                
                
        return False