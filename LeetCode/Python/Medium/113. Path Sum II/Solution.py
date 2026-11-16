# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        def preorder(root, total, lst, ans):
            if not root:
                return []

            total += root.val
            lst.append(root.val)
            if not root.left and not root.right and total == targetSum:
                    ans.append(lst[:])
            
            preorder(root.left, total,lst, ans)
            preorder(root.right, total,lst, ans)
            
            lst.pop()
            
        ans = []
        preorder(root, 0, [],ans)
        return ans