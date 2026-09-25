# # Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self):
        self.head = None
        
    
        
    def addTwoNumbers(self, l1:ListNode, l2:ListNode) -> ListNode:
        s1 =""
        while l1:
            s1 += str(l1.val)
            l1 = l1.next
        
        s1 = s1[::-1]  
        
        s2 =""
        while l2:
            s2 += str(l2.val)
            l2 = l2.next
        
        s2 = s2[::-1] 
        
        total = list(str(int(s1) + int(s2))[::-1])
        
        j = dummy =  ListNode()
        
        for i in total:
            j.next = ListNode(i)
            j = j.next
        return dummy.next



