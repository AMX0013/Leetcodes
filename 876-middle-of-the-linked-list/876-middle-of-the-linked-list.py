# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        byOne = head
        byTwo = head
        end = False
        
        while byTwo != None:
            byTwo=byTwo.next
            
            if byTwo != None:
                byTwo=byTwo.next
                byOne= byOne.next
        return byOne
            
        