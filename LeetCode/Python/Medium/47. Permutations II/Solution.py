class Solution:
    def uniquePermutation(self, nums, ind, ans):
        if ind == len(nums):
            ans.append(nums[:])
            return 
        for i in range(ind, len(nums)):
            if i > ind and nums[i] == nums[ind]: continue
            nums[ind], nums[i] = nums[i], nums[ind]
            self.uniquePermutation(nums, ind + 1, ans)
            nums[ind], nums[i] = nums[i], nums[ind]

    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        ans  = []
        nums.sort()
        self.uniquePermutation(nums, 0, ans)
        return ans
        