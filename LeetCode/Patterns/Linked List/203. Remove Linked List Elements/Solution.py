# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = head
        prev = ListNode(0,None)
        if head == None:
            return head
        while head is not None and head.val == val:
            head = head.next
        while temp:
            if temp.val == val:
                prev.next = temp.next
            if temp.val != val:    
                prev = temp   
            temp = temp.next
        return head
