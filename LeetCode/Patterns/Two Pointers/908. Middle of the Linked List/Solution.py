# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
  
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
        #   count_node = 0
        # temp = head
        # while temp:
        #     count_node += 1
        #     temp = temp.next
        # middle_count = count_node // 2
        # count_node = 0
        # temp2 = head
        # while temp2:
        #     if count_node == middle_count:
        #         return temp2
        #     temp2 = temp2.next
        #     count_node += 1