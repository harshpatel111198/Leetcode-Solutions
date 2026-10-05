class Solution:
    def myPow(self, x: float, n: int) -> float:
        # return x**n
        N = abs(n)
        def recursion(n):
            if n == 0:
                return 1
            temp = recursion(n // 2)
            if n % 2 ==0:
                return temp * temp
            else:
                return x * temp * temp
        
        ans = recursion(N) 
        return ans if n > 0 else 1 / ans        
        