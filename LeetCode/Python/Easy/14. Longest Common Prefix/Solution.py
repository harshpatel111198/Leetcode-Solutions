class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = float('inf')
        for s in strs:
            if len(s) < min_length:
                min_length = len(s)
      
        ind = 0
        while ind < min_length:
            for s in strs:
                if s[ind] != strs[0][ind]:
                    return s[:ind]
            ind += 1
        if len(strs) <= 1:
            return strs[0]
        else:
            return strs[0][:ind]