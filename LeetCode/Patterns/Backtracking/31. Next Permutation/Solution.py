class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind = -1
        for i in range(len(nums)-1,0,-1):
            if nums[i] > nums[i-1]:
                ind = i - 1
                break
        if ind == -1:
            return nums.reverse()
        for j in range(len(nums)-1,ind,-1):
            if nums[j] > nums[ind]:
                nums[ind], nums[j] = nums[j], nums[ind]
                break
        left = ind + 1
        right = len(nums)-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    
        

        
        