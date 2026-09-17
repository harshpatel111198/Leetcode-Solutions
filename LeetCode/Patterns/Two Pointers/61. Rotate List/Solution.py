# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        length = 1
        curr = head
        if not head or not head.next:
            return head
        while curr.next:
            curr = curr.next
            length += 1
        
        k = k % length 
        if k == 0:
            return head
        
        curr.next = head

        steps = length - k
        new_tail = head
        for _ in range(steps - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None
        # for i in range(k):
        #     curr = head
        #     while curr.next.next:
        #         curr = curr.next
        #     temp = curr.next
        #     curr.next.next = head
        #     curr.next = None
        #     head = temp
        return new_head
             