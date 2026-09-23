# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        curr = head
        dummyNode = ListNode(-1, head)
        prev = dummyNode
        while curr and curr.next:
            if curr.val < curr.next.val:
                prev = curr
                curr = curr.next
                continue
            while curr and curr.next and curr.val == curr.next.val:
                curr = curr.next

            prev.next = curr.next
            curr = prev.next
        return dummyNode.next
