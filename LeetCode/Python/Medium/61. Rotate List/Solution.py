# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        length = 0
        curr = head
        if not head or not head.next:
            return head
        while curr:
            curr = curr.next
            length += 1
        
        k = k % length if k > length else k
        for i in range(k):
            curr = head
            while curr and curr.next.next:
                curr = curr.next
            temp = curr.next
            curr.next.next = head
            curr.next = None
            head = temp
        return head
             