import queue
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        res = []
        tempQ = queue.Queue(maxsize=10001)
        HEIGHT = 0
        if root == None:
            
            return HEIGHT
        tempQ.put(root)
        
        while (tempQ.empty() == False ):
            #1 get size = no. of elements in queue
            size = tempQ.qsize()
            #2 for all elements that are in the queue, add their left and right nodes into queue
            i=0
            tempArr = []
            while i < size:
                nodes = tempQ.get()
                if(nodes.children != None):
                    childs = nodes.children
                    for child in childs:
                        tempQ.put(child)
                
                
                tempArr.append(nodes.val)
                i+=1
            res.append(tempArr)
            HEIGHT+=1
        return HEIGHT
        