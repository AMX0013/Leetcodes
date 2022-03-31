class Solution:
        
    def solve(self, own ,index,prices, memo,count) -> int:
        default = 0
        
        if index == len(prices) :
            return default
        if count<=0:
            return default
        #print( index ,own , prices[index],">",memo)
        #print(index,own,count)
        if memo[count][index][own] != None:
            return memo[count][index][own]
        if own == 1:    # if a stock is  owned on day i > find max(selling that stock and call it again or hold the stock and call func again for next day)
            
            profit1 = prices[index] + self.solve(0,index+1,prices,memo,count-1) #sell
            profit2 = self.solve(1,index+1,prices,memo,count) #hold
            memo[count][index][own] = max(profit1,profit2) 
            #print("own ==1","profit = ",max(profit1,profit2),profit1,profit2 ,index ,own , prices[index],">",memo)
            return memo[count][index][own]
            
            
        else: # if a stock is not owned on day i > find max(buying that stock and call it again or dont buy and call func again for next day)
            
            profit1 = -(prices[index]) + self.solve(1,index+1,prices,memo,count) #buy
            profit2 = self.solve(0,index+1,prices,memo,count) #skip
            memo[count][index][own] = max(profit1,profit2) 
            #print("own ==0","profit = ",max(profit1,profit2),profit1,profit2 ,index ,own , prices[index],">",memo)
            return memo[count][index][own]
    def maxProfit(self, prices: List[int]) -> int:
        a = 2
        b = len(prices)
        c=3
        memo = [[ [None for col in range(a)] for col in range(b)] for row in range(c)] # memo = [[None]*cols]*rows <this broke the memo : 
        #print(memo[0][0][2])
        #print("initial:",memo)
        x=self.solve(0,0,prices,memo,2)
        #print("Final:",memo)
        return x