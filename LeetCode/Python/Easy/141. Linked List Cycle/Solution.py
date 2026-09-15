# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
        slow = head
        q = set()
        while node:
            if node.next in q:
                return True
            q.add(node.next)
            node = node.next
        q = set()
        return False
        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next

        #     print(fast,slow)
        #     if fast == slow:
        #         return True
        # return False