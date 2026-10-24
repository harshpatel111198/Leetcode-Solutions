class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        left, right, bottom, top  = 0, m-1, n-1, 0
        res = []
        while top <= bottom and left <= right:
            #right
            for i in range(left,right+1):
                res.append(matrix[top][i])
            top += 1
        
            #bottom
            for i in range(top,bottom+1):
                res.append(matrix[i][right])
            right -= 1

            # print(top,bottom,left,right)
            
            #left
            if top <= bottom:
                for i in range(right,left-1,-1):
                    res.append(matrix[bottom][i])
                bottom -= 1
        
            #top
            if left <= right:
                for i in range(bottom, top-1,-1):
                    res.append(matrix[i][left])
                left += 1

        return res        