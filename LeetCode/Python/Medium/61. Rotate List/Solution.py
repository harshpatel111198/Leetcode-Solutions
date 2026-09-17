# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        node = head
        dummy = node
        ln = 0
        
        while dummy:
            ln+=1
            dummy = dummy.next

        rotation = k%ln
        for i in range(rotation):
            while node:
                if node.next.next is None:
                    node.next.next = head
                    head = node.next
                    node.next = None
                node = node.next
            node = head
        return head