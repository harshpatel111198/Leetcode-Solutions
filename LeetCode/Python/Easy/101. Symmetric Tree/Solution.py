# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        
        stack1 = []
        stack2 = []
        curr1 = root
        curr2 = root
        while curr1 and curr2:
            while curr1:
                stack1.append(curr1)
                curr1 = curr1.left
            while curr2:
                stack2.append(curr2)
                curr2 = curr2.right
            curr1 = stack1.pop()
            curr2 = stack2.pop()
            if curr1.val != curr2.val:
                return False
            curr1 = curr1.right
            curr2 = curr2.left
        return True
