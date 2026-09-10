class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = set()
        for i in range(len(nums)):
            hash_map = {}
            for j in range(i+1,len(nums)):
                k = -(nums[i] + nums[j]) 
                if k in hash_map.values():
                    tup = tuple(sorted([nums[i], nums[j], k]))
                    res.add(tup)
                hash_map[i+j] = nums[j]
           
        return list(res)