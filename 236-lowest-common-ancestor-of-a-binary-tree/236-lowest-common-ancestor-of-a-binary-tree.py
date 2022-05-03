# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
from queue import Queue

class Solution:
    '''      
    def nodeExplorer(self,node,nodesList):
        nodesList.append(node.val) #adds node value as the VAlue attribue of the dict
        if node.left!= None:
            self.nodeExplorer(node.left,nodesList)
        if node.right != None:
            self.nodeExplorer(node.right,nodesList)
        return None
    
    def treeMapper(self,node,treeMap):
        nodesList= []
        self.nodeExplorer(node,nodesList)
        nodesList.pop(0)
        treeMap[node] = nodesList  #adds node value as the Key attribue of the dict
    '''
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def nodeSearch(node):
            if not node: # basically None nodes
                return
            l= None
            r = None
            
            if node == p or node ==q:
                print(node.val)
                return node
            
            l = nodeSearch(node.left)
            r = nodeSearch(node.right)
            
            if l and r:
                print("res:",node.val)
                return node
            
            return l or r # to further penetrate the branches where p or q was found
        
        return nodeSearch(root)
        '''
        
        
        
        treeMap = defaultdict(list)
        qx = Queue(maxsize=9999)
        
        qx.put(root)
        #bfs = []
        while qx.empty() != True:
            size = qx.qsize()
            for i in range(size):
                node = qx.get()
                self.treeMapper(node,treeMap)
                #bfs.append(node)
                if node.left!= None:
                    qx.put(node.left)
                if node.right!= None:
                    qx.put(node.right)
                
                
                    
            
                
        #bfs / level ordser traversal to maintain order
        
        res = None    
        
        print(treeMap)

        print(p,q)

        if q.val in treeMap[p]:
            print("Q in P")
            res = p
            
            return res
        if p.val in treeMap[q]:
            print("P in Q")
            res = q
            return res
        else:
            print("TBD")
            for i in treeMap:
                
                if p.val in treeMap[i] and q.val in treeMap[i]:
                    #if q.val in treeMap[i]:
                    res = i
                    print(i)
                


            print("res = ",res)
            return res
                
                
        
        
        #100000
        '''
        