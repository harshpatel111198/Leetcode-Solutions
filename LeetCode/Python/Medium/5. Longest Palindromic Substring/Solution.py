class Solution:
#     def longestPalindrome(self, s):
        
       
#         # palindrome = [s[i:j+1] for i in range(len(s)) for j in range(len(s)) if s[i:j+1] ==  "".join(reversed(s[i:j+1])) and len(s[i:j+1])>0]
      
#         palindrome1 = [s[i:j+1] for i in range(len(s)) for j in range(len(s)) ]
#         # palindrome2 = [ i for i in palindrome1 if i == i[::-1] if len(i)>0]
        
        

#         # print(palindrome2)
#         # for i in range(len(s)):
#         #      for j in range(len(s)):
#         #             reverse = s[i:j+1]
#         #             if (s[i:j+1] == reverse[::-1]) and (len(s[i:j+1])>0):
#         #                     palindrome.append(s[i:j+1])
        
#         return max([ i for i in palindrome1 if i == i[::-1] if len(i)>0], key=len)
                        
        
        
        def longestPalindrome(self, s):
            res = ""
            for i in range(len(s)):
                # odd case, like "aba"
                tmp = self.helper(s, i, i)
                if len(tmp) > len(res):
                    res = tmp
                # even case, like "abba"
                tmp = self.helper(s, i, i+1)
                if len(tmp) > len(res):
                    res = tmp
            return res

        # get the longest palindrome, l, r are the middle indexes   
        # from inner to outer
        def helper(self, s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1; r += 1
            return s[l+1:r]