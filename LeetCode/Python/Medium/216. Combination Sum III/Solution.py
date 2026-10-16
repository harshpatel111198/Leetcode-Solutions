class Solution:
    def getCombination(self, k, n, ind, total, lst, ans):
        if len(lst) == k:
            if total == n:
                ans.append(lst[:])
                return
            else:
                return
        for i in range(ind, 10):
            lst.append(i)
            total += i
            self.getCombination(k, n, i + 1, total, lst, ans)
            lst.pop()
            total -= i
            
        
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        ans = []
        self.getCombination(k, n, 1, 0, [], ans)
        return ans
        