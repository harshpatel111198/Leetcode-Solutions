class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # k = k%len(nums)
        # nums.reverse()
        # nums[:k] = nums[:k][::-1]
        # nums[k:] = nums[k:][::-1]
        k = k%len(nums)
        temp = nums[-k:]
        for i in range(len(nums)-k-1,-1,-1):
            nums[i+k] = nums[i]
        for j in range(k):
            nums[j] = temp[j]      




        