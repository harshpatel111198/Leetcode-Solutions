class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        reverse_num = 0
        num = abs(x)
        while num  > 0:
            digit = num % 10
            reverse_num = reverse_num * 10 + digit
            num = num // 10
        if sign * reverse_num > 2**31 -1 or sign * reverse_num < -2**31:
            return 0 
        return sign * reverse_num