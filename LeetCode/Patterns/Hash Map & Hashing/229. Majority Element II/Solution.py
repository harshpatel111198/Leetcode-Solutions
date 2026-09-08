class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        frequency = {}
        res = []
        appearance = len(nums)//3 + 1
        for n in nums:
            frequency[n] = frequency.get(n, 0) + 1
            
            if frequency[n] == appearance:
                res.append(n)
            
            if len(res) == 2:
                break
            
        return res