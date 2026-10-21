class Solution:
    def getkthPermutation(self, ind, nums, ans):
        if  ind == len(nums):
         
            ans.append(nums[:])
            return

     
        for i in range(ind, len(nums)):
            nums[ind], nums[i] = nums[i], nums[ind]
            
            self.getkthPermutation(ind + 1, nums, ans)
            nums[ind], nums[i] = nums[i], nums[ind]
        
    def getPermutation(self, n: int, k: int) -> str:

        nums = list(range(1, n+1))
       
        ans = []
        self.getkthPermutation(0, nums, ans)
        ans = sorted(ans)[k-1]
        res = "".join(map(str, ans))
        return res
        