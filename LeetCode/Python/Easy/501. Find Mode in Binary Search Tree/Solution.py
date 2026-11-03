# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode | None) -> list[int]:
        res = []
        prev_max = 0
        curr_max = 0
        prev_ele = 0
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()

            if prev_ele == curr.val:
                curr_max += 1
                if prev_max < curr_max:
                  
                    res.clear()
                
                    res.append(curr.val)
                    prev_max = max(curr_max, prev_max)
                    prev_ele = curr.val
                    curr_max = 1
                
            else: 
                prev_max = max(curr_max, prev_max)
                prev_ele = curr.val
                curr_max = 1
                if curr_max > prev_max:
                    res.append(curr.val)
            if prev_max == curr_max:
                    if curr.val not in res:
                        res.append(curr.val)
                    print(res)
                
            # freq_map[curr.val] = freq_map.get(curr.val, 0) + 1
           
            curr = curr.right
        # max_val = max(freq_map.values())
    
        # res = [k for k, v in freq_map.items() if v == max_val]

        return res