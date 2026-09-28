# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        dummyNode = ListNode(-1)
        lesserValue = dummyNode
        dummyNode1 = ListNode(0)
        greaterValue = dummyNode1
        curr = head
        while curr:

            while curr and curr.val < x:
                lesserValue.next = curr
                lesserValue = lesserValue.next
                curr = curr.next
            while curr and curr.val >= x:
                greaterValue.next = curr
                greaterValue = greaterValue.next
                curr = curr.next
        greaterValue.next = None
        lesserValue.next = dummyNode1.next
        return dummyNode.next 
      
       