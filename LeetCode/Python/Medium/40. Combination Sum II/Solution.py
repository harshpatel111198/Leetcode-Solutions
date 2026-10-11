class Solution:
    def findPairs(self, candidates, list_len, target, ind, lst, ans):
            
            if target == 0:
                    ans.append(lst[:])
                    return
            for i in range(ind,list_len):
                if i > ind and candidates[i] == candidates[i-1]:continue
                if candidates[i] > target:break

                lst.append(candidates[i])
                self.findPairs(candidates, list_len, target - candidates[i], i + 1, lst, ans)
                lst.pop()

    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        candidates.sort()
        self.findPairs(candidates, len(candidates), target, 0, [], ans)
     
        return ans
        