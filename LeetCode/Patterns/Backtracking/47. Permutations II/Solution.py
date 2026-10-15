class Solution:
    def uniquePermutation(self, nums, lst, ans, extra_lst):
        if len(lst) == len(nums):
            ans.append(lst[:])
            return 
        for i in range(0, len(nums)):
            if extra_lst[i]: continue
            if i > 0 and nums[i] == nums[i-1] and not extra_lst[i-1]: continue
            extra_lst[i] = 1
            lst.append(nums[i])
            self.uniquePermutation(nums, lst, ans, extra_lst)
            extra_lst[i] = 0
            lst.pop()
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()
        self.uniquePermutation(nums, [], ans, [0]*len(nums))
        return ans
        