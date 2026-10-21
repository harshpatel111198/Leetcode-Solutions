class Solution:
    def palindromePartition(self, s, ind, lst, ans):
        if ind == len(s):
            ans.append(lst[:])
            return
        for i in range(ind, len(s)):
            if s[ind:i+1] == s[ind:i+1][::-1]:
                lst.append(s[ind:i+1])
                self.palindromePartition(s, i + 1 , lst, ans)
                lst.pop()

    def partition(self, s: str) -> list[list[str]]:
        ans = []
        self.palindromePartition(s,0, [], ans)
        return ans
