class Solution:
    def numSquares(self, n: int) -> int:
        memo = []
        
        if n ==0:
            return 0
        j=0

        while j <=n:
            memo.append(j)
            j+=1
        
        x = 1
        while x<= n:

            i = 1
            while i*i <=  x:
                memo[x] = min( memo[x], 1+memo[x-i*i])
                i+=1
            x+=1
        

        return memo[n]