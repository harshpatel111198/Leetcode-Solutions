# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        slow = fast = head
        prev = slow
        if not head.next:
            return None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev and prev.next and prev.next.next:
            prev.next = prev.next.next
        else:
            prev.next = None
        print(prev)
        return head