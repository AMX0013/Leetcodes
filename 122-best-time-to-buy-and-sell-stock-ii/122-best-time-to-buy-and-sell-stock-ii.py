class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit2 = 0
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
                    
                
                
            
            


        
        
        return profit2
        