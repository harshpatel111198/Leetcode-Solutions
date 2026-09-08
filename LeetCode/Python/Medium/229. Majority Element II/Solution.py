class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt1, cnt2 = 0, 0
        el1 = float("-inf")
        el2 = float("-inf")

        for i in range(len(nums)):
            if cnt1 == 0 and nums[i] != el2:
                cnt1 = 1
                el1 = nums[i]
            elif cnt2 == 0 and nums[i] != el1:
                cnt2 = 1
                el2 = nums[i]
            elif el1 == nums[i]:
                cnt1 += 1
            elif el2 == nums[i]:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        res = []
        cnt1, cnt2 = 0, 0
        for n in nums:
            if n == el1:cnt1 += 1
            if n == el2:cnt2 += 1
        mini = (len(nums) // 3) + 1
        if cnt1 >= mini:res.append(el1)
        if cnt2 >= mini:res.append(el2)
        return res