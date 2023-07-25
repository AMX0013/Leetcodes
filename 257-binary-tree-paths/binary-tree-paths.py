# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        memo = {}

        def recurDfs(node) :
            resList = []
            print("for :",node.val)
            

            if node.left == None and node.right == None:
                res = ""
                res += str(node.val)
                resList.append(res)
            else:

                if node.left != None:
                    
                    subTree = recurDfs(node.left)
                    for nodes in subTree:
                        leftRes = ""
                        leftRes +=str(node.val)

                        leftRes += "->"
                        leftRes += str(nodes)

                        print("for :",node.val,"leftRes :", leftRes)
                        resList.append(leftRes)

                if node.right != None:
                    
                    subTree = recurDfs(node.right)
                    for nodes in subTree:
                        rightRes = ""
                        rightRes +=str(node.val)
                        rightRes += "->"
                        rightRes += str(nodes)
                        
                        print("for :",node.val,"rightRes :", rightRes)
                        resList.append(rightRes)
            print(resList)   
            return resList

        myRes = recurDfs(root)
        print(myRes)

        return myRes
            

                    
