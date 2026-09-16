# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        slow = fast = head
        total = 0
        while fast and fast.next:
            total += slow.val
            slow = slow.next
            fast = fast.next.next
        middle_slow = slow.val
        while slow:
            total -= slow.val
            slow = slow.next
        if total == 0:
            return True
        return False

