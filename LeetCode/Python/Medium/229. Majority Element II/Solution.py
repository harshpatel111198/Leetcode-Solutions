class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        frequency = {}
        res = []
        for n in nums:
            frequency[n] = frequency.get(n, 0) + 1
            appearance = len(nums)//3
            if frequency[n] > appearance:
                res.append(n)
        return res