class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_len = 0
        l = 0
        #maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            #maxf = max(maxf, count[s[r]]) if use this, no need to scan whole hashmap
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
        
        return max_len

        # time: O(26*n)
        # space: O(26)