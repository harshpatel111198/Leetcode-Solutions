# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: ListNode | None, k: int) -> list[ListNode | None]:
        res = []
        total_nodes = 0
        temp = head
        while temp:
            total_nodes += 1
            temp = temp.next
        no_el = total_nodes // k
        no_extra_el = total_nodes % k
        temp = head
        for i in range(no_extra_el):
            tempHead = temp
            for j in range(no_el):
                temp = temp.next
            res.append(tempHead)
            tempHead = temp.next
            temp.next = None
            temp = tempHead
        print(temp)
        for i in range(k-no_extra_el):
            if temp:
                tempHead = temp
                for j in range(no_el-1):
                    if temp:
                        temp = temp.next
                    else:
                        break
                res.append(tempHead)
                tempHead = temp.next
                temp.next = None
                temp = tempHead
            else:
                res.append(ListNode())
        return res
        