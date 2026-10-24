class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        a = n
        left, right, bottom, top = 0, a-1, a-1, 0
        res = [[0]*n for i in range(n)]
        num = 1

        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                res[left][i] = num
                num += 1
            top += 1

            for i in range(top, bottom + 1):
                res[i][right] = num 
                num += 1
            right -= 1
            
            for i in range(right, left - 1, -1):
                res[bottom][i] = num
                num += 1
            bottom -= 1

            for i in range(bottom, top - 1, -1):
                res[i][left] = num
                num += 1
            left += 1
        return res

