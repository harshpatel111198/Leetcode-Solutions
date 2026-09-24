# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        curr = head
        dummy = ListNode(-1, head)
        prev = dummy
        while curr and curr.next: 
            prev = curr
            while curr and curr.next and curr.val == curr.next.val:
                curr = curr.next

            prev.next = curr.next
            
            curr = curr.next
        return dummy.next