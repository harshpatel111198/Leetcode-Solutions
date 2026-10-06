class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        b =  int("".join(map(str, b)))
        b = int(b)
        
        def recursion(b):

            if b == 0:
                return 1
            temp = recursion(b // 2)

            if b % 2 == 0:
                return temp * temp
            else:
                return a * temp * temp
        
        return recursion(b) % 1337