import queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        height = 0
        if root == None:
            return height
        
        tempQ = queue.Queue(maxsize = 10001)
        
        tempQ.put(root)
        height+=1
        while (tempQ.empty() == False):
            
            i=0
            size = tempQ.qsize()
            while i < size:
                
                node = tempQ.get()
                if node.left != None:
                    tempQ.put(node.left)
                if node.right != None:
                    tempQ.put(node.right)
                if node.right == None and node.left == None: 
                    return height
                
                    
                i+=1
            height+=1
            
        return height
        