class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
            lst = list(num)
            for k_times in range(k):
                ind = -1
                for i in range(len(lst)-1, 0, -1):
                    if int(lst[i]) > int(lst[i-1]):
                        ind = i - 1
                        break

                # if ind == -1:
                #     lst[::] = lst[::-1]
                for j in range(len(lst)-1, ind, -1):
                    if int(lst[j]) > int(lst[ind]):
                        temp = lst[ind]
                        lst[ind] = lst[j]
                        lst[j] = temp
                        break
                left = ind + 1
                right = len(lst) - 1
                while left < right: 
                    lst[left], lst[right] = lst[right], lst[left]
                    left += 1
                    right -= 1
            i  = j = 0
            cnt = 0
            while i < len(num) and j < len(lst):
                while num[i] != lst[j]:
                    j += 1
                while i != j:
                    cnt += 1
                    lst[j], lst[j-1] = lst[j-1], lst[j]
                    j -= 1
                i += 1
                j += 1
            return cnt



            
            return 0
        