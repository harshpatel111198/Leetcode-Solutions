# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        hash_map = {}
        cnt = 0
        while fast is not None and fast.next is not None:
            if slow == fast.next:
                return True
            # hash_map[cnt] = slow.val
            slow = slow.next
            fast = fast.next.next
        else:
            return False