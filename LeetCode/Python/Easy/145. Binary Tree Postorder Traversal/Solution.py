# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []    
        cur = root
        post_order = []
        while cur or len(stack)>0:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                temp = stack[-1].right
                if temp is None:
                    while len(stack) > 0 and temp == stack[-1].right:
                        temp = stack.pop()
                        post_order.append(temp.val)
                else:
                    cur = temp
        return post_order