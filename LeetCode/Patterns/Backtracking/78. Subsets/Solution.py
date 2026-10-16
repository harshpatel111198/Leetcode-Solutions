class Solution:
    def findSubsets(self, nums, nums_len, ind, lst, ans):
        if ind > nums_len - 1:
            return

        for i in range(ind, nums_len):
            
            lst.append(nums[i])
            ans.append(lst[:])
            self.findSubsets(nums, len(nums), i + 1, lst, ans)
            lst.pop()
        self.findSubsets(nums, len(nums), i + 2, lst, ans)
            
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()
        ans.append([])
        self.findSubsets(nums, len(nums), 0, [], ans)
        return ans