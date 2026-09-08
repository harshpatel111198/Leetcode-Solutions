class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        el = nums[0]
        for i in range(0,len(nums)):
            if count == 0:
                el = nums[i]
                count += 1
            elif el != nums[i]:
                count -= 1
            else:
                count += 1
        return el
        # count1 = 0
        # for i in range(len(nums)):
        #     if el == nums[i]:
        #         count1 += 1
        # if count1 > len(nums)//2:
        #     return el