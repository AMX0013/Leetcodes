class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        R=0
        rows = max(prices)+1
        profit = 0
        profit2 = 0
        #memo =[[0]*rows]*rows
        while R < len(prices):
            
            if prices[R] < prices[L]:
                L= R
                
                
            if prices[L] < prices[R]:
                                             
                res = prices[R] - prices[L]

                if profit < res:
                    profit = res
            
            R+=1
        L=0
        R=1
        while L < len(prices) and R < len(prices):
            
            if prices[L] < prices[R]:                                             
                res = prices[R] - prices[L]
                profit2 += res
                L+=1
                R+=1
            else:
                L+=1
                R+=1
                    
                
                
            
            


        
        
        return max(profit,profit2)
        