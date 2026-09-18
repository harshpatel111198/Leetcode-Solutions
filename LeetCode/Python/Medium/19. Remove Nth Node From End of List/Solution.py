# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self,head: ListNode, n: int) -> ListNode:
        itr = head
        s =""
        count =0
        list_conversion = []
        
        while itr:
            list_conversion.append(itr.val)
            itr = itr.next
        # while itr:
        #     if count ==0:
        #         node = ListNode(itr.val,None)
        #         count += 1
        #         itr = itr.next
        #         head = node
        #     else:
        #         node = ListNode(itr.val,head)
        #         itr =itr.next
        #         head = node
        #         count += 1
        
        
#         itr2 = head 
#         l =[]
#         count1 = 1
#         while itr2:
#             l.append(itr2.val)
            
            # if count1 == 1 and n == 1:
            #     print(itr2.val)
            #     itr2 = itr2.next
            #     return
            # if count1 == count-1 and itr2.next.next is None:
            #     itr2.next = None
            #     break
            # if count1 == n-1:
            #     itr2.next = itr2.next.next
            #     break
            
            
            # count1 += 1
            # itr2 = itr2.next
        l1 = list_conversion[::-1]
        l2 = []
        for i in range(len(l1)):
            if i != n-1:
                l2.append(l1[i])
        
        
        
        j = dummy = ListNode(0)   
        for i in l2[::-1]:
            j.next = ListNode(i)
            j = j.next
        return dummy.next
    