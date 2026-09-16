# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findMid(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        prev = nxt = None
        curr = self.findMid(head)
        # reverse the other half side
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # get the max sum of twin nodes
        rightHead = prev
        leftHead = head
        max_sum = 0
        
        while rightHead:
            max_sum = max(max_sum, rightHead.val + leftHead.val)
            leftHead = leftHead.next
            rightHead = rightHead.next
        return max_sum
