class Solution:
    def chooseStep(self, cost , stairSize, index, memo):
        if memo[index]:            
            return memo[index]
        if index == stairSize-1 or index== stairSize-2:
            return cost[index]
        res = cost[index] + min( self.chooseStep(cost , stairSize, index+1, memo) , self.chooseStep(cost , stairSize, index+2, memo) )
        
        memo[index] = res
        return res
        
        
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        stairSize = len(cost)
        
        memo = {}        
        for i in range(stairSize+2):
            memo[i] = None
        
        
        return min( self.chooseStep(cost , stairSize, 0, memo) , self.chooseStep(cost , stairSize, 1, memo) )
            
        
        
        
        