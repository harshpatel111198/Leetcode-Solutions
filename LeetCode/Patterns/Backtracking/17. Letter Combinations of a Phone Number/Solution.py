import itertools
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        tel_num_str = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        list_comb = []
        for i in digits:

            list_comb.append(list(tel_num_str[int(i)]))
        combinations = []
        if len(list_comb) == 1:
            combinations = [''.join(comb) for comb in product(list_comb[0])]
        elif len(list_comb) == 2:
            combinations = [''.join(comb) for comb in product(list_comb[0],list_comb[1])]
        elif len(list_comb) == 3:
            combinations = [''.join(comb) for comb in product(list_comb[0],list_comb[1],list_comb[2])]
        elif len(list_comb) == 4:
            combinations = [''.join(comb) for comb in product(list_comb[0],list_comb[1],list_comb[2],list_comb[3])]
        else:
            return combinations
        return combinations
        
    