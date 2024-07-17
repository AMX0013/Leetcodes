# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        # iterate over the nodes DFS
        # if node.left or node.right is to be deleted
            # tbd = node.left or node.right
            # store tbd in res
            # call DFS on them again
        res = []     
        

        def dfs( node: TreeNode):
            # if this node is to be deleted
            # create a bool var sav_child 
            sav_child = False

            if node.val in to_delete:
                # remove node from res
                sav_child = True
                if node in res:
                    res.remove(node)
            
            if node.left:
                LFT = node.left
                # disconnect child if it is to be deleted first.
                #  We will still move to res, for future deletion
                if LFT.val in to_delete:                    
                    node.left = None
                # if parent is deleted, move child into res.
                if sav_child:
                    res.append(LFT)
                # explore the child noneheless
                dfs(LFT)

                

            if node.right:
                RHT = node.right
                # disconnect child if it is to be deleted first.
                #  We will still move to res, for future deletion
                if RHT.val in to_delete:                    
                    node.right = None
                # if parent is deleted, move child into res.
                if sav_child:
                    res.append(RHT)
                # explore the child noneheless
                dfs(RHT)
                
                
                
        res.append(root)
        dfs(root)
        
        return res
                
            

        