# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLL(self, curr):
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return curr
    def getkthNode(self, curr, k):
        k -= 1
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        curr = head
        nextNode = None
        prevLast = None
        while curr:
           # finding the kth Node
            kthNode = self.getkthNode(curr, k)
            if not kthNode:
                if prevLast:
                    prevLast.next = curr
                break
            
            #separate the kth group and reverse
            nextNode = kthNode.next
            kthNode.next = None

            self.reverseLL(curr)

            if curr == head:
                head = kthNode
            else:
                prevLast.next = kthNode
            
            
            prevLast = curr
            curr = nextNode
        return head