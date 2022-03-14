class Solution:  
        
    def genSteps(self, n,memo):
        if memo[n]:            
            return memo[n]        
        if n== 1 or n== 0:
            res = 1
        else:
            res = self.genSteps(n-1,memo) + self.genSteps(n-2,memo)
        
        memo[n] = res      
        return res   
        
    def climbStairs(self, n: int) -> int:
        memo = {}        
        for i in range(n+1):
            memo[i] = None
        
        x = self.genSteps(n,memo)
        print(x)
        return x
        