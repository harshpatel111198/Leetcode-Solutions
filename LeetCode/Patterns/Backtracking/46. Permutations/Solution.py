class Solution:
    def allPairs(self, nums, lst, ans):
        if len(lst) == len(nums):
            ans.append(lst[:])
            return
        
        for i in range(0, len(nums)):
            if nums[i] in lst : continue
            lst.append(nums[i])
            
            self.allPairs(nums, lst, ans)
            lst.pop()
            
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []
        self.allPairs(nums, [], ans)
        return ans