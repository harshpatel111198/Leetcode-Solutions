class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        i = 0
        length = len(arr)

        while i < length - 1 and arr[i] < arr[i+1]:
            i += 1
        
        if i == 0 or i == length - 1:
            return False
        
        while i < length - 1 and arr[i] > arr[i+1]:
            i += 1
        
        return i == length - 1
        
            