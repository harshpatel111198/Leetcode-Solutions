class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        length = len(arr)
        if length < 3:
            return False
        high = 0
        for i in range(1,length):
            if arr[high] < arr[i]:
                high = i
            elif arr[high] == arr[i]:
                return False
            else:
                break
        if high not in range(1,length-1):
            return False
        for j in range(high+1, length-1):
            if arr[j] <= arr[j+1]:
                return False
        return True

        


