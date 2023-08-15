# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        # Defualt creates [0]

        left = ListNode()
        right = ListNode()

        if head == None:
            return head
        leftHead = left
        rightHead = right

        while head!= None:
            if head.val < x:
                left.next = head
                left = left.next
                # print("left",left)

            else:
                right.next = head
                right = right.next
                # print("right",right)


            head = head.next

        print(left,right)
        right.next = None
        left.next = rightHead.next
        return leftHead.next