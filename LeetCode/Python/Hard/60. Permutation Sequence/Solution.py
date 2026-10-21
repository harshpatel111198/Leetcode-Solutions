class Solution:
    def getkthPermutation(self, k, ind, cnt, nums, ans):
        if  ind == len(nums):
            ans.append(nums[:])
            return
        print(k, nums)
        for i in range(ind, len(nums)):
            nums[ind], nums[i] = nums[i], nums[ind]
            
            self.getkthPermutation( k-1, ind + 1, cnt + 1, nums, ans)
            nums[ind], nums[i] = nums[i], nums[ind]
        
    def getPermutation(self, n: int, k: int) -> str:

        nums = list(range(1, n+1))
       
        ans = []
        self.getkthPermutation( k, 0, 0, nums, ans)
        return "".join(map(str,ans[k-1]))
        