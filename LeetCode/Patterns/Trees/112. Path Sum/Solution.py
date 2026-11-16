# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        def preorder(root, total):
            if not root:
                return False

            total += root.val

            if not root.left and not root.right:
                return total == targetSum     
            # total -= root.val
        

            return preorder(root.left, total) or preorder(root.right, total)
        
        return preorder(root, 0)