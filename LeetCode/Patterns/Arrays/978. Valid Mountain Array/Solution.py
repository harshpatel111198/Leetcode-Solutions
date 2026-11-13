class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        high = 0
        for i in range(1,len(arr)):
            if arr[high] < arr[i]:
                high = i
            elif arr[high] == arr[i]:
                return False
            else:
                break
        if high not in range(1,len(arr)-1):
            return False
        for j in range(high+1, len(arr)-1):
            if arr[j] <= arr[j+1]:
                return False
        return True

        


