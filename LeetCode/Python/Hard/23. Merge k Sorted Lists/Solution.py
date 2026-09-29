# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lst = []
        if lists is None:
            return lists
        for i in lists:
            while i:
                lst.append(i.val)
                i = i.next
        
        dummy1 = dummy2 = ListNode(0)
        for i in sorted(lst):
            dummy1.next = ListNode(i)
            dummy1 = dummy1.next
        return dummy2.next