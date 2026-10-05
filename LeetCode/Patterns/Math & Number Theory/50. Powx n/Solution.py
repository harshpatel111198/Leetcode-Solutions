class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n
        # if n == 0:
        #     return x
        # if n > 0:
        #     return self.myPow(, n - 1)
        # if n < 0:
        #     return self.myPow(1/(x*x), n + 1)