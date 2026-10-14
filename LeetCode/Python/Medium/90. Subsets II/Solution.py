class Solution:
    def findSubsets(self, nums, nums_len, ind, lst, ans):
        ans.append(lst[:])

        for i in range(ind, nums_len):
            if i != ind and nums[i] == nums[i-1]:continue
            
            lst.append(nums[i])
            
            self.findSubsets(nums, len(nums), i + 1, lst, ans)
            lst.pop()
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()
        self.findSubsets(nums, len(nums), 0, [], ans)
        return ans