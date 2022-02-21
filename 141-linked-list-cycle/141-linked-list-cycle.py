# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        itr1 = head
        if head == None:
            return False
        itr2 = head.next
        #print(head(0))
        if head == None:
            return False
        try:
            while  itr1.next != None and  itr2.next.next != None and  itr2.next != None:
                if itr1 == itr2:
                    return True
                else:
                    itr1 = itr1.next
                    itr2 = itr2.next.next
        except:
            return False

        return False
            
            