# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        prev1 = prev2 = None
        curr1 = l1
        curr2 = l2
        while curr1 or curr2:
            if curr1:
                front1 = curr1.next
                curr1.next = prev1
                prev1 = curr1
                curr1 = front1
            if curr2:
                front2 = curr2.next
                curr2.next = prev2
                prev2 = curr2
                curr2 = front2
        
        dummy = ListNode(-1)
        curr = dummy
        
        carry = 0
        while prev1 or prev2:
            total = 0
            if prev1 and prev2:
                total = prev1.val + prev2.val + carry
                prev2 = prev2.next
                prev1 = prev1.next
            elif prev1:
                total = prev1.val + carry
                prev1 = prev1.next
            elif prev2:
                total = prev2.val + carry
                prev2 = prev2.next
                
            carry = total // 10
            total = total % 10
            
            

            curr.next = ListNode(total)
            curr = curr.next
        res = dummy.next
        prev = None
        while res:
            front = res.next
            res.next = prev
            prev = res
            res = front
        return prev