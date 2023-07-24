# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
       
        dp = {}

        dp[0] = []
        dp[1] = [TreeNode()]


        if n%2 == 0:
            return None
        
        def backTrackingTreeGen(n):
            
            # print("--------",n,"-------")
                
            if n in dp:
                # print(">",dp[n])
                return dp[n]

            res = []

            for l in range(n):
                r = n-1-l

                leftRes , rightRes = backTrackingTreeGen(l) , backTrackingTreeGen(r)
                
                # print(leftRes , "---", rightRes)
                for arrsL in leftRes:
                    for arrsR in rightRes:
                        res.append(TreeNode(0 , arrsL , arrsR)) 
            dp[n] = res
            return res
                

        res = backTrackingTreeGen(n)
        # print(res)
        # for key in dp.keys():
            # print("dp[",key,"] :",dp[key])
        return res
