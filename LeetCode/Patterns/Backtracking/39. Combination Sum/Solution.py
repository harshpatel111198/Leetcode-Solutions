class Solution:

    def findPairs(self, candidates, list_len, target, ind, lst, ans):
            if ind > list_len-1 or target < 0:
                return
            if target == 0:
                ans.append(lst[:])
                return
              

            lst.append(candidates[ind])
            self.findPairs(candidates, list_len, target - candidates[ind], ind, lst, ans)

            lst.pop()
            self.findPairs(candidates, list_len, target, ind + 1, lst, ans)
           
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
     
        ans = []
        self.findPairs(candidates, len(candidates), target, 0, [], ans)
        return ans
        