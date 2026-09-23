# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        frquency_map = {} 
        curr = head
        prev = None
        while curr:
            frquency_map[curr.val] = frquency_map.get(curr.val, 0) + 1
            curr = curr.next
        print(frquency_map)
        curr = ListNode(-1)
        dummy = curr
        for key in frquency_map.keys():
            if frquency_map[key] == 1:
                curr.next = ListNode(key)
                curr = curr.next

        return dummy.next