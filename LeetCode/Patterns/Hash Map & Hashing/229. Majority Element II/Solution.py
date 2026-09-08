class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        frequency = {}
        res = set()
        appearance = len(nums)//3
        for n in nums:
            frequency[n] = frequency.get(n, 0) + 1
            
            if frequency[n] > appearance:
                res.add(n)
        return list(res)