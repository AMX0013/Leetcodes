# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:


        def recurNodeHunt(node ,val):

            if node.val == val:
                return "Y"
            
            elif node.left == None and node.right== None:
                return ""

            else:
                leftPath = ""
                rightPath = ""
                if node.left != None:
                    # print("debugError before",node.left.val)
                    leftPath = recurNodeHunt(node.left, val)
                    

                    if  len( leftPath) >0 :
                        
                        leftPath ='L' + leftPath

                if node.right != None:
                    rightPath = recurNodeHunt(node.right, val)                    
                    if  len(rightPath) >0:
                        rightPath = 'R' + rightPath

            

                return    leftPath + rightPath    

        srcPath  = recurNodeHunt(root,startValue)
        destPath = recurNodeHunt(root,destValue)

        print(srcPath , destPath)
        # must find common root?
        s = 0
        d = 0
        while srcPath[s] == destPath[d]:
            s+=1
            d+=1
        
        sPath = srcPath[s:-1]
        dPath = destPath[d:-1]

        print(sPath,dPath )

        res = 'U'*len(sPath) + dPath
        return res



        



  























        
        # finalRes = ""

        # def recurNodeHunt(node ,src,dest):
        #     # Entring

        #     print("---------------------------Entering" , node.val)
        #     leftPath = ""
        #     rightPath = ""
        #     compute = True

        #     if node.val == src :
        #         res = ""
        #         res += "src"
        #         return res , True

        #     if node.val == dest :
        #         res = ""
        #         res += "dst"
        #         return res , True

        #     if node.left == None and node.right== None and (node.val != src or node.val != dest) :
        #         print(node.val , "return "",False ")
        #         return "" , False
            

        #     else:
        #         if node.left != None:
        #             # print("debugError before",node.left.val)
        #             leftPath , Lcompute = recurNodeHunt(node.left, src , dest)
                    

        #             if  len( leftPath) >0 :
        #                 if Lcompute:
        #                     leftPath ='L' + leftPath
        #             print("debugError after",node.val , "L'received ' + leftPath" , leftPath)

        #         if node.right != None:

        #             rightPath , Rcompute = recurNodeHunt(node.right, src , dest)

                    
        #             if  len(rightPath) >0:
                        
        #                 if Rcompute:
        #                     rightPath = 'R' + rightPath
        #             print(node.val ,"received" , rightPath , Rcompute)

        #     # if len( leftPath) >0 and  len(rightPath) >0:
        #     #     compute = False
        #     #     # Curr node would be the root of the subtree having shortest path
        #     #     # Now we identify which of these paths are to be converted completely to UPs
        #     #     # Done by checking arr[-1] == src
        #     #     print("Sol idnetified with subtree of subRoot : ", node.val)
        #     #     print(leftPath, leftPath[-3:], rightPath ,rightPath[-3:]) 
        #     #     if leftPath[-3:] == 'src':
        #     #         # convert all elements of leftPath to U
        #     #         n = len(leftPath) -3
        #     #         leftPath = 'U'*n
        #     #         res = leftPath + rightPath[:-3]
        #     #         print("res = ", res ," at subtree of subroot" , node.val)
        #     #         return res , compute
        #     #     elif rightPath[-3:] == 'src' :
        #     #         # convert all elements of rightPath to U
        #     #         n = len(leftPath) -3
        #     #         rightPath = 'U'*n
        #     #         res = rightPath + leftPath[:-3]
        #     #         print("res = ", res ," at subtree of subroot" , node.val)
        #     #         return res , compute
                
        #     #     # fianlRes = res
        #     # else:
        #     #     if len(leftPath) >0:
        #     #         print("len(leftPath) >0",len(leftPath) >0)
        #     #         print(len(rightPath)>0)
        #     #         return leftPath , compute
        #     #     elif len(rightPath)>0:
        #     #         print("len(rightPath)>0",len(rightPath)>0)
        #     #         print(len(leftPath) >0)
        #     #         return rightPath , compute

            
        #     print("uncaught condition for ",node.val)
        #     print("---------------------------Exiting" , node.val)

        #     return "" , compute
        #     # return #Once global var is populated

        # if root.val == startValue:
        #     startValue = 0
        #     print("startValue = 0",startValue )
        # if root.val == destValue:
        #     print("destValue = 0",destValue )
        #     destValue = 0

        # finalRes , _ = recurNodeHunt(root,startValue,destValue)
        
        
        # if startValue == 0:
        #     return finalRes[:-3]
        # elif destValue == 0:
        #     newLen = len(finalRes)-3
        #     newRes = 'U'*newLen
        #     return newRes

        # print("returnedVal = ", finalRes)
        # return finalRes



                
                        


            