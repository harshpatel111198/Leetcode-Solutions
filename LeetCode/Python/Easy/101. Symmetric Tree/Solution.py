# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if not root:
            return True
            
        # Stack stores pairs of nodes that should be mirror images of each other
        stack = [(root.left, root.right)]
        
        while stack:
            left, right = stack.pop()
            
            # If both are None, this path is symmetric; continue checking others
            if not left and not right:
                con
                
            # If only one is None, or their values don't match, it's asymmetric
            if not left or not right or left.val != right.val:
                return False
                
            # Push children in mirrored pairs:
            # 1. Outer children: left's left with right's right
            # 2. Inner children: left's right with right's left
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))
            
        return True