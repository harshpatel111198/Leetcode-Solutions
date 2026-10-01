class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) ==1:
            return True
        start = nums[0]
        i =0
        while i < len(nums)-1 or (nums[i]==0 and i != len(nums)-1):  
          i = i + nums[start]
          start = i
          
        if start == len(nums)-1:
            return True
        else:
            False