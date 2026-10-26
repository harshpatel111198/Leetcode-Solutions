class Solution:
    def allParenthesisPairs(self, n, opened, close, strs, ans):
        if len(strs) == 2 * n:
            ans.append(strs)
            return

        if opened < n:
                self.allParenthesisPairs(n, opened + 1, close, strs + "(", ans)
        if close < opened:
                self.allParenthesisPairs(n, opened, close + 1, strs + ")", ans)

    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        self.allParenthesisPairs(n, 0, 0, "", ans)
        return ans