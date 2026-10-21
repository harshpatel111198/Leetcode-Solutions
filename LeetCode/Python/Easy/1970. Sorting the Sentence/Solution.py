class Solution:
    def sortSentence(self, s: str) -> str:
        lst = s.split(" ")
        ans = ["0"]*len(lst)
        for s in lst:
            ans[int(s[-1])-1] = s[:-1]
        ans = " ".join(ans)
        return ans