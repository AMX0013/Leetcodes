import queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
         
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        tempQ = queue.Queue(maxsize=2001)
        
        if root == None:
            
            return res
        tempQ.put(root)
        
        while (tempQ.empty() == False ):
            #1 get size = no. of elements in queue
            size = tempQ.qsize()
            #2 for all elements that are in the queue, add their left and right nodes into queue
            i=0
            tempArr = []
            while i < size:
                nodes = tempQ.get()
                if(nodes.left != None):
                    tempQ.put(nodes.left)
                if(nodes.right != None):
                    tempQ.put(nodes.right)
                
                tempArr.append(nodes.val)
                i+=1
            res.append(tempArr)
        return res
                
                    
            
        
        
        
        