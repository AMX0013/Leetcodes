# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # we arent in a binary SEARCH Tree
        # p and q can have a common LCA orr,
        # p and q can be the LCA themselves as well

        # LCA = None

        def recur(node:TreeNode):
            # this will go left and right
            # we need to find 2 nodes, so lets use a sum, to indicate if both are found
            # print("At node:", node.val)
            LCA = None
            found = 0
            L,R = 0, 0

            if node == p or node == q:
                # p!= q so just 1 value found
                found +=1
                print("Found", found, "th", LCA)
                

            if node.left:
                L,L_LCA = recur(node.left)
                
                LCA = LCA or L_LCA

            if node.right:
                R,R_LCA = recur(node.right)
                # due to precedence, this could override LCA with None
                LCA = LCA or R_LCA


            found += L+R

            if found == 2:
                print(found, "mfs found,", "LCA is I", node.val)
                LCA = node
                return 0, LCA

            return found, LCA

        found, LCA = recur(root)

        return LCA
        