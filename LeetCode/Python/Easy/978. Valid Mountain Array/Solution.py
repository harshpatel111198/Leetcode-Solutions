class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        length = len(arr)
       
        high = 0
        while high+1 < length and arr[high] < arr[high+1]:
            high+=1
        if high == 0 or high == length-1:
            return False
        while high+1 < length and arr[high] > arr[high+1]:
            high+=1
        return high == length-1
        # for i in range(1,length):
        #     if arr[high] < arr[i]:
        #         high = i
        #     elif arr[high] == arr[i]:
        #         return False
        #     else:
        #         break
        # if high not in range(1,length-1):
        #     return False
        # for j in range(high+1, length-1):
        #     if arr[j] <= arr[j+1]:
        #         return False
        # return True

        


