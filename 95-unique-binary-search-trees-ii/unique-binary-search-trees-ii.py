# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def recurGenTrees(left,right):
            # case when n = 1: left , right = 1
            # In this case, the tree would be [ [`1`]]
            if left == right:
                return [TreeNode(left)]

            # Case when generating subtrees, 
            # Left half = left,val-1
            # right half = val+1 to right
            # root = val

            # In case when we reach leaf, left > val-1 or val+1 > right
            if left > right: 
                return [None]

            res = []
            # Treemaykr:

            # rootSel
            for val in range(left,right+1):
                # genLeft
                for leftSubTree in recurGenTrees(left,val-1):
                    # genRight
                    for rightSubTree in recurGenTrees(val+1,right):

                        root = TreeNode(val,leftSubTree,rightSubTree)
                        res.append(root)
            return res
        
        resTrees = recurGenTrees(1,n)

        # print(resTrees)

        return resTrees