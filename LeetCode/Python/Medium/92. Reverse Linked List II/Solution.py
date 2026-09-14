# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        temp = head
        count = 0
        prev = temp
        temp2 = None
        node = None
        while temp.next:
            count += 1
            temp2 = temp.next

            if count == left:
                while temp2 and count <= right:
                    t = temp2.next
                    temp2.next = node
                    node = temp2
                    temp2 = t
                    count += 1  
            prev.next = node
            temp = temp.next
            break
        head = prev
        while prev.next is not None:
            prev = prev.next
        prev.next = temp2
        return head
