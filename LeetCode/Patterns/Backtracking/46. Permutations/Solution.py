class Solution:
    def allPairs(self, nums, lst, ans, extra_list):
        if len(lst) == len(nums):
            ans.append(lst[:])
            return
        
        for i in range(0, len(nums)):
            if nums[i] in lst : continue
            lst.append(nums[i])
            extra_list[i] = 1
            self.allPairs(nums, lst, ans, extra_list)
            lst.pop()
            extra_list[i] = 0
   
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []
        self.allPairs(nums, [], ans, [0]*len(nums))
        return ans