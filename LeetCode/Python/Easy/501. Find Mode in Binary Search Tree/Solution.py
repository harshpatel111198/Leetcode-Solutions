# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode | None) -> list[int]:
        freq_map = {}
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            
            freq_map[curr.val] = freq_map.get(curr.val, 0) + 1
           
            curr = curr.right
        max_val = max(freq_map.values())
        print(max_val, freq_map)
        res = [k for k, v in freq_map.items() if v == max_val]

        return res