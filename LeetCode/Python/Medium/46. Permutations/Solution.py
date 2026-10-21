class Solution:
    def allPairs(self, nums, ind, ans):
        if ind == len(nums):
            ans.append(nums[:])
        
        for i in range(ind, len(nums)):
            nums[ind], nums[i] = nums[i], nums[ind]
            self.allPairs(nums, ind + 1, ans)
            nums[ind], nums[i] = nums[i], nums[ind]
         
            
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []
        self.allPairs(nums, 0, ans)
        return ans