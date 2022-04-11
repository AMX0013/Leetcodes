import queue
class Solution:
    def postOrder(self, node, potres , height,dictTree):
        left  = None
        right = None
        if node.left != None:
            self.postOrder(node.left , potres, height+1,dictTree)
            left = node.left.val
            
        if node.right != None:
            self.postOrder(node.right , potres, height+1,dictTree)
            
            right = node.right.val
        dictTree[height].append(node)
        potres.append([node.val,height,[left,right],node])
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        temp = root
        print("--------------")
        height = 0
        arr = []
        dictTree = {i:[] for i in range(1001)}
        
        self.postOrder(root,arr,0,dictTree)
        
        parser = []
        subResult = []
        for items in arr:
            
            if items[1] > height:
                height = items[1]
        
        while height >=0:
            if height == 0:
                return root
            if len(dictTree[height]) == 1:
                return dictTree[height][0]
            else:
                subroot = []
                for node in dictTree[height-1]:
                    if node.left in dictTree[height] or node.right in dictTree[height]:
                        subroot.append(node)
                dictTree[height-1] = subroot
                height -=1





        
        
        '''
        for items in arr:
            print(items[0],items[1],items[2])
        unfound = True
        '''
        
        
        '''
        
        
        for i in range(1001):
            if dictTree[i]:
                print(dictTree)
        if len(parser) ==1:
            print("1")
            return parser[0][1]
        elif len(parser) ==2:
            for items in arr:
                if items[2] == subResult: # convenient lca
                    print("2")
                    return items[3]
                else: # traverse above to find a common root
                    print("3")
                    return root
                    #while unfound:
                        
                        
        else:
            print("3")
            return root
                                  
       '''                           
            