class Solution:
    
    def solve(self, own ,index,prices, memo,fee) -> int:
        default = 0
        
        if index >= len(prices) :
            return default
        #print( index ,own , prices[index],">",memo)
        if memo[index][own] != None:
            return memo[index][own]
        if own == 1:    # if a stock is  owned on day i > find max(selling that stock and call it again or hold the stock and call func again for next day)
            
            profit1 = prices[index] + self.solve(0,index+2,prices,memo,fee) #sell
            profit2 = self.solve(1,index+1,prices,memo,fee) #hold
            memo[index][own] = max(profit1,profit2) 
            #print("own ==1","profit = ",max(profit1,profit2),profit1,profit2 ,index ,own , prices[index],">",memo)
            return memo[index][own]
            
            
        else: # if a stock is not owned on day i > find max(buying that stock and call it again or dont buy and call func again for next day)
            
            profit1 = -(prices[index]+fee) + self.solve(1,index+1,prices,memo,fee) #buy
            profit2 = self.solve(0,index+1,prices,memo,fee) #skip
            memo[index][own] = max(profit1,profit2) 
            #print("own ==0","profit = ",max(profit1,profit2),profit1,profit2 ,index ,own , prices[index],">",memo)
            return memo[index][own]
    def maxProfit(self, prices: List[int]) -> int:
        cols = 2
        rows = len(prices)
        memo = [[None]*cols for i in range(rows)] # memo = [[None]*cols]*rows <this broke the memo : 
        #print(memo)
        x=self.solve(0,0,prices,memo,0)
        #print("Final:",memo)
        return x
        