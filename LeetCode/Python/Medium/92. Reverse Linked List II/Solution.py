# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        leftPrev, cur = dummy, head
        # reach node at position left
        for i in range(left-1):
            leftPrev, cur = cur, cur.next
        
        # reverse the nodes from left to right
        prev = None
        for i in range(right - left + 1):
            tempNxt = cur.next
            cur.next = prev
            prev = cur
            cur = tempNxt
        
        # update the pointers
        leftPrev.next.next = cur # cur is node after right
        leftPrev.next = prev # prev is right

        return dummy.next
