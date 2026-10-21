class Solution:
    def allPairs(self, nums, lst, ans):
        if len(lst) == len(nums):
            ans.append(lst[:])
            return
        
        for i in range(0, len(nums)):
            if nums[i] in lst : continue
            lst.append(nums[i])
            
            self.allPairs(nums, lst, ans)
            lst.pop()
        
    def getPermutation(self, n: int, k: int) -> str:

        nums = list(range(1, n+1))
       
        ans = []
        self.allPairs(nums, [], ans)
    
        return "".join(map(str,ans[k-1]))
        