# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        switch = 1
        if not root:
            return []
        queue = [root]
        ans = []
        
        while queue:
            size = len(queue)
            temp = [0] * size
            hold = []
            for i in range(size):
                node = queue.pop(0)
                if switch:
                    temp[i] = node.val
                else:
                    temp[size - i - 1] = node. val

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            # if switch:
            #     switch = 0
            # else:
            #     # temp.reverse()
            #     switch = 1
            switch = 0 if switch else 1
            ans.append(temp)
        return ans
            
            

                