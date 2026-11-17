class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = nums[-k:]

        for i in range(len(nums)- k - 1, -1, -1):
            nums[i + k] = nums[i] 

        for i in range(len(temp)):
            nums[i] = temp[i]