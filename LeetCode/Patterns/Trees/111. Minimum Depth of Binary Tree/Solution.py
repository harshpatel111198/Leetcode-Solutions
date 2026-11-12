# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        queue = [root]
        height = 0
        while queue:
            height += 1
            size = len(queue)
            for _ in range(size):
                node = queue.pop(0)

                if not node.left and not node.right:
                    return height
                
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
        return height