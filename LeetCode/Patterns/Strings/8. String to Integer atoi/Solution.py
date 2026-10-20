class Solution:
    def myAtoi(self, s: str) -> int:
        pre_char = {" ", "+"}
        # hash_map = {"1":1,"2":2,"3",3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"0":0,"-":-}
        res = ""
        for char in s:
            print(char) 
            if char in pre_char:
                continue
            elif char == ".":
                break
            elif len(res) == 0 and char == "-":
                res += char
            elif (char == "-" or char == "+") and len(res) != 0 and res[-1] in "0123456789":
                break
            elif char == "0" and len(res) != 0 and res[-1] not in "123456789":
                continue
            elif char.isalpha():
                break
            elif char.isdigit():
                res += char
        
        result = 0
        if len(res) == 0:
            return 0
        start_idx = 1 if res[0] in ("-", "+") else 0
        for i in range(start_idx, len(res)):
            char = res[i]
           
                
            # Extract the integer value using ASCII math
            digit = ord(char) - ord('0')
            result = (result * 10) + digit
        INT_MIN = -2147483648
        INT_MAX = 2147483647
        result = -result if res[0] == "-" else result
        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN
        return result