class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        lst = s.split(" ")
        num = -1
        for i in range(len(lst)):
            if lst[i].isdigit():
                
                if num >= int(lst[i]):
                    return False
                num = int(lst[i])

        return True