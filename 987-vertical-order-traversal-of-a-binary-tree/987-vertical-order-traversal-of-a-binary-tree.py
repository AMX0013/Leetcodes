# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def nodeMapper(self,node, depth, width, matrix):
        matrix[width][depth].append(node.val)
        
        if node.left != None:
            self.nodeMapper(node.left, depth+1, width-1, matrix)
        if node.right != None:
            self.nodeMapper(node.right, depth+1, width+1, matrix)
        return None
            
    def treeWidthFinder(self,node,width,depth,widthsArr,heightArr):
        widthsArr.append(width)
        heightArr.append(depth)
        if node.left != None:
            self.treeWidthFinder(node.left,width-1, depth+1,widthsArr,heightArr)
        if node.right != None:
            self.treeWidthFinder(node.right,width+1, depth+1,widthsArr,heightArr)
        return None
    
    
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        widthsArr = []
        heightArr=[]
        initialW = 0
        
        self.treeWidthFinder(root,0,0,widthsArr,heightArr)
        left = min(widthsArr)
        right = max(widthsArr)
        height = max(heightArr)
        l=0
        r = -1*left + right
        mid = l+abs(left)        
        
        print(left,right,"mid:",mid,"max height : ",height,"rightmost",r )
        
        matrix = [[[] for i in range(height+1) ]for j in range(r+1)]
        
        res = []
        self.nodeMapper(root, 0, mid, matrix)
        for wid in range(r+1):
            print(matrix[wid])
            tempRes = []
            for dep in range(height+1):
                matrix[wid][dep].sort()
                temp = matrix[wid][dep]
                
                print(">",temp)
                if temp:
                    for i in temp:
                        print(">=",i)
                        tempRes.append(i)
            if tempRes:
                res.append(tempRes)
        
        return res
                
                
                
        
        
        
        
        
        
        