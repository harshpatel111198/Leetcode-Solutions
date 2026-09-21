# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeLL(self, left, right):
        dummyNode = ListNode(-1)
        temp = dummyNode

        while left and right:
            if left.val < right.val:
                temp.next = left
                temp = left
                left = left.next 
            else:
                temp.next = right
                temp = right
                right = right.next
        if left:
            temp.next = left
        else:
            temp.next = right
        return dummyNode.next

    def findmiddle(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def mergeSort(self, head):
        if not head or not head.next:
            return head
        middle = self.findmiddle(head)
        leftHead = head
        rightHead = middle.next
        middle.next = None

        leftHead = self.mergeSort(leftHead)
        rightHead = self.mergeSort(rightHead)

        return self.mergeLL(leftHead, rightHead)
    def sortList(self, head: ListNode | None) -> ListNode | None:
       
        # lst = []
        # temp = head
        # while temp:
        #     lst.append(temp.val)
        #     temp = temp.next

        # lst.sort()
        # print(lst)
        # temp = head
        # i = 0
        # while temp:
        #     temp.val = lst[i]
        #     i += 1
        #     temp = temp.next
        

        return self.mergeSort(head)