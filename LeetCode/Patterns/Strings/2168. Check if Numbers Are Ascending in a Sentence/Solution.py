class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        lst = list(s.split(" "))
        num_lst = [0]
        for s in lst:
            if s.isdigit():
                num_lst.append(int(s))
        i = num_lst[0]
        for num in num_lst[1:]:
            if num <= i:
                return False
            else:
                i = num
        return True