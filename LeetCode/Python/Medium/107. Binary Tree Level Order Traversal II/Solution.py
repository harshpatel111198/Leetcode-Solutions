# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        
        queue = [root]
        ans = []
        while queue:
            size = len(queue)
            temp = []
            for _ in range(size):
                node = queue.pop(0)

                temp.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
                
            ans.insert(0, temp)

        return ans