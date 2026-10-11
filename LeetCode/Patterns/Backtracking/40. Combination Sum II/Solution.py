class Solution:
    def findPairs(self, candidates, list_len, target, ind, lst, ans):
            
            if ind == list_len:
                if target == 0:
                    ans.append(lst[:])
                return
           

            if candidates[ind] <= target:
                lst.append(candidates[ind])
                self.findPairs(candidates, list_len, target - candidates[ind], ind + 1, lst, ans)
                lst.pop()
            
            self.findPairs(candidates, list_len, target, ind + 1 , lst, ans)

    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        self.findPairs(candidates, len(candidates), target, 0, [], ans)
        seen = set()
        unique_pairs = []
        for pair in ans:
        # Sort the pair and convert to a tuple so it can be added to the set
            normalized = tuple(sorted(pair)) 
            if normalized not in seen:
                seen.add(normalized)
                unique_pairs.append(pair)
        return unique_pairs
        