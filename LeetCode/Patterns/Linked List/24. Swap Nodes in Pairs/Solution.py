# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if not head and not head.next: return head

        curr = head
        dummyNode = ListNode(-1, head)
        prev = dummyNode
        while curr and curr.next:
          # save ptrs
          second = curr.next
          nextPair = curr.next.next

          # swap the current pair
          prev.next = second
          second.next = curr
          curr.next = nextPair

          # set pointers for next pairs
          prev = curr
          curr = nextPair

        return dummyNode.next

            