class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        i = 0
        while i < len(arr):
            if i < len(arr) - 1 and arr[i] == arr[i + 1]:
                return False
            if i < len(arr) - 1 and arr[i] > arr[i + 1]:
                i += 1
                break
            i += 1
        if i >= len(arr) - 1:
            return False
        while i < len(arr):
            if i < len(arr) - 1 and arr[i] <= arr[i+1]:
                return False
            i += 1
        return True
        
            