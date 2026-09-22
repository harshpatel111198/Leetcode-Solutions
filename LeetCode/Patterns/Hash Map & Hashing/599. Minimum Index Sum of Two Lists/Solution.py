class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        hash_ind = {}
        res = []
        min_ind = float("inf")
        for i in range(len(list1)):
            hash_ind[list1[i]] = i
        
        for i in range(len(list2)):
            if list2[i] in hash_ind:
                temp = i + hash_ind[list2[i]]
                if temp < min_ind:
                    res = []
                    min_ind = temp
                    res.append(list2[i])
                elif temp == min_ind:
                    res.append(list2[i]) 
        return res