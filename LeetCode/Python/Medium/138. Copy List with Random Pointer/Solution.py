"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def insertCopyNode(self, head):
        temp = head
        while temp:
            newNode = ListNode(temp.val)
            newNode.next = temp.next
            temp.next = newNode
            temp = temp.next.next
        return head
    def addRandomPointer(self, head):
        temp = head
        while temp:
            newNode = temp.next
            if temp.random:
                newNode.random = temp.random.next
            else:
                newNode.random = None
            temp = temp.next.next
        return head
    def deepCopyLL(self, head):
        dummy = ListNode(-1)
        res = dummy
        temp = head
        while temp:
            res.next = temp.next
            temp.next = temp.next.next

            temp = temp.next
            res = res.next
        return dummy.next
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        insertedNode = self.insertCopyNode(head)
        head_added_random = self.addRandomPointer(insertedNode)
        return self.deepCopyLL(head_added_random)