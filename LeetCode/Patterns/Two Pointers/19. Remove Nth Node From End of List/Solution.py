# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        length = 1
        curr = head
        while curr.next:
            curr = curr.next 
            length += 1
        
        if length == 1 and n == 1:
            return None
        n_node = 0
        curr = head
        while curr:
            n_node += 1
            if length - n_node == n:
                curr.next = curr.next.next
                break
            curr = curr.next
        return head
