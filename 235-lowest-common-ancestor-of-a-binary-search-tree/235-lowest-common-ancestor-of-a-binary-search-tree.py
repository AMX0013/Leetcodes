# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node):
            l = None
            r = None
            
            #1 node exists
            if not node:
                return
            
            l = dfs(node.left)
            r = dfs(node.right)
            
            if node == p or node ==q:
                return node # called by node.left or node.right
            
            if l and r:
                return node # the node whose l and r exists
            
            # we reach the end if we dont find l and r > as either l or r dont exist
            # from root, there always will be l or r found
            # >> therefore we must go back to a node that is found
            return l or r
        return dfs(root)