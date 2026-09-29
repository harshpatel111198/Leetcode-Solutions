# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode | None) -> TreeNode | None:
        if not head or not head.next:
            return head
        prev = None
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            front = slow.next
            slow.next = prev
            prev = slow
            slow = front
        

        res = TreeNode(slow.val)
        temp = res
        slow = slow.next
        right = None
        fast = slow
        while slow:
            front = slow.next
            slow.next = right
            right = slow
            slow = front 
        while prev:
                if temp.val > prev.val:
                    temp.left = TreeNode(prev.val)
                    temp = temp.left
                else:
                    temp.right = TreeNode(prev.val)
                    temp = temp.right
                prev = prev.next
        temp = res
        while right:
            if temp.val < right.val:
                temp.right = TreeNode(right.val)
                temp = temp.right
            else:
                temp.left = TreeNode(right.val)
                temp = temp.left
            right = right.next
      
        return res          