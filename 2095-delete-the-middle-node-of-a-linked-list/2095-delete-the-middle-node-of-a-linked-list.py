# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.header = None
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        byOne = None
        byTwo = None
        temp = None
        byOne = head
        byTwo = head
        
        self.header = head
        if self.header.next == None:
            return self.header.next
        temp=self.header
        
        while byTwo != None:
            byTwo=byTwo.next
            
            if byTwo != None:
                byTwo=byTwo.next
                byOne= byOne.next
                
        while temp.next != byOne:
            temp = temp.next
        temp.next = byOne.next
            
        # need to attach the middle of the LL to byOne
        
        return self.header