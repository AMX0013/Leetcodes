# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = None
        # This is easy because its a binary search tree
        # p and q are going to be around their LCA such that p LCA q ORR q LCA p
        # OUR Goal is to ensure that we go left or right based on the common side that both p and q exist
            
        curr_ptr = root

        while curr_ptr:
            # ensure mutual exclusivit through usage of if elif else
            
            if p.val < curr_ptr.val and q.val < curr_ptr.val:
                # move left and check
                curr_ptr = curr_ptr.left
            
            elif p.val > curr_ptr.val and q.val > curr_ptr.val:
                # move right
                curr_ptr = curr_ptr.right
            
            # if both have failed, then currptr is between p and q
            else:
                return curr_ptr