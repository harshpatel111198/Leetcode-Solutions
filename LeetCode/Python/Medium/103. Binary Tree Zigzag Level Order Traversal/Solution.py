# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        switch = 0
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
                if switch == 1:
                 
                    if node.left:
                        queue.append(node.left)
                
                    if node.right:
                        queue.append(node.right)
                else:
                    if node.right:
                        queue.append(node.right)
                
                    if node.left:
                        queue.append(node.left)
            ans.append(temp)
            if switch == 0:
                switch = 1
            else:
                switch = 0
        return ans
            
            

                