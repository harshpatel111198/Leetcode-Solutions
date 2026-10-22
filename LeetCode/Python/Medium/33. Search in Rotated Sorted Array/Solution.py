class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            left_target = abs(target - nums[l])
            right_target = abs(target - nums[r])
            if left_target == right_target:
                return -1
            if left_target > right_target:
                l = l + (r - l) // 2
            else:
                r = r - (r - l) // 2
        return -1
