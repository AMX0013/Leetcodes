# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        node = head.next
        nextZero = False
        while node.next:
           
            # while node.next.val !=0 and node.next:
            if node.next.val==0:
                if not node.next.next:
                    node.next = node.next.next
                    return head.next
                # print("at 0",node)
                # print()
                node = node.next
            # print("at node:",node.val,node)
            if node.next:
                node.val += node.next.val
                node.next = node.next.next
                # print("now node is:",node.val,node.next)

        