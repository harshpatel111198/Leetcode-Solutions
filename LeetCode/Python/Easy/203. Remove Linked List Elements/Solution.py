# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ans = ListNode(0, head)
        temp = ans
        while temp:
            while temp.next and temp.next.val == val:
                temp.next = temp.next.next
            temp = temp.next
        return ans.next
        # prev = ListNode(0,None)
        # if head == None:
        #     return head
        # while head is not None and head.val == val:
        #     head = head.next
        # while temp:
        #     if temp.val == val:
        #         prev.next = temp.next
        #     if temp.val != val:    
        #         prev = temp   
        #     temp = temp.next
        # return head
