# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def findMid(self,head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def isPalindrome(self, head: ListNode | None) -> bool:
       
        if not head or not head.next:
            return True
        # if fast has node then there are odd number of nodes.
        # if fast:
        #     slow = slow.next
        # reverse the half side
        prev = None
        curr = self.findMid(head)
        nxt = None
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        rightHead = prev
        leftHead = head
        while rightHead:
            if rightHead.val != leftHead.val:
                return False
            rightHead = rightHead.next
            leftHead = leftHead.next
        return True
