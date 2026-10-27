class Solution:
    def reorganizeString(self, s: str) -> str:
        dct = {}
        l = [""]*len(s)
        for char in s:
            dct[char] = dct.get(char,0) + 1

        sorted_chars = sorted(dct.keys(),key=lambda x: dct[x], reverse = True)

        if dct[sorted_chars[0]] > (len(s)+1)//2:
            return ""

        ind = 0
        for char in sorted_chars:
            for _ in range(dct[char]):
                if ind > len(s)-1:
                    ind = 1
                l[ind] = char
                ind += 2

                
        return "".join(l)