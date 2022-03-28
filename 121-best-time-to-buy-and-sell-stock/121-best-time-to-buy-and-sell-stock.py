class Solution:
        
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        R=0
        rows = max(prices)+1
        profit = 0
        #memo =[[0]*rows]*rows
        while R < len(prices):
            
            if prices[R] < prices[L]:
                L= R
                
                
            if prices[L] < prices[R]:
                                             
                res = prices[R] - prices[L]

                if profit < res:
                    profit = res
            
            R+=1

                    
            #print("L,R >", L,R," memo[",prices[L],",",prices[R], "] >" ,prices[R] - prices[L])
        return profit


            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''
        rows, cols = (len(prices),len(prices))
        memo = [[0]*cols]*rows
        maxi=0
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                memo[i][j] = prices[j]-prices[i]
                #print("i,j>",prices[i],prices[j],"profit>",memo[i][j])
                if memo[i][j] > maxi:
                    maxi = memo[i][j]
        #print(memo)
        return maxi
        '''
        
        
                
        