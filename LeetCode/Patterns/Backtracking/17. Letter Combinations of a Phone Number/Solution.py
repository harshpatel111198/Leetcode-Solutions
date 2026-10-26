class Solution:
    def allLetterCombinations(self, hash_map, digits, strs, ind, ans):
        if ind == len(digits):
            ans.append(strs)
            return
        curr_digit = digits[ind]
        letters = hash_map[curr_digit]

        for ch in letters:
                self.allLetterCombinations(hash_map, digits, strs + ch, ind + 1, ans)

    
    def letterCombinations(self, digits: str) -> list[str]:
        hash_map = {"2":"abc", "3":"def", "4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        ans = []
        self.allLetterCombinations(hash_map, digits, "", 0, ans)
        return ans