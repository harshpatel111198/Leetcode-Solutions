class Solution:
    def findSubsets(self, nums, nums_len, ind, lst, ans):
        if ind > nums_len - 1:
            return

        for i in range(ind, nums_len):
            if i > ind and nums[i] == nums[i-1]:continue
            
            lst.append(nums[i])
            ans.append(lst[:])
            self.findSubsets(nums, len(nums), i + 1, lst, ans)
            lst.pop()
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        ans = []
        ans.append([])
        nums.sort()
        self.findSubsets(nums, len(nums), 0, [], ans)
        return ans