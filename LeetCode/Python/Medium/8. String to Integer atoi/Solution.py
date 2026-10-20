class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        #white space
        while i < n and s[i] == ' ':
            i += 1
        #sign
        sign = 1
        if i < n and (s[i] == '-' or s[i] == '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        result = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            result = result * 10 + digit
            if result * sign > 2**31 - 1:
                return 2**31 - 1
            if result * sign < -2**31:
                return -2**31
            i += 1
        return result * sign
        