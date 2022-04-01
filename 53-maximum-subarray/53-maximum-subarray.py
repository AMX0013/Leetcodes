import math
class Solution:
    def recursiveSolve(self, nums, beginSub,index, memo):
        '''
        
        # > prevents decision to be made for the last element
        if index == len(nums)-1 :
            return nums[index]
        '''    
        if index >= len(nums):
            return -math.inf
        if memo[index][beginSub] != None:
            return memo[index][beginSub]
        
        if beginSub ==1: #SubArray has started and 1 or more elements have been added
            #1>  add current element and stop
            res1 =  nums[index]
            #2> add current element and continue adding >
            res2 =nums[index]+ self.recursiveSolve(nums,1,index+1,memo)
            #3> stop immediately
            
            memo[index][beginSub] = max(res1,res2)
            return memo[index][beginSub]
            
        else: #Subarray has not yet started
            #1 > lets add this element and start the SubArray from it or start and end it right away
            res1 = max(nums[index]+ self.recursiveSolve(nums,1,index+1,memo)   ,   nums[index]+ 0)
            #2 > skip this element 
            res2 = self.recursiveSolve(nums,0,index+1,memo)
            memo[index][beginSub] = max(res1,res2)
            return memo[index][beginSub]
        
    def maxSubArray(self, nums: List[int]) -> int:
        cols = 3 # 0,1,2 are the states of beginSub
        rows = len(nums)
        memo = [[None]*cols for i in range(rows)]
        #print(memo)
        #print("----------")
        sol = self.recursiveSolve(nums,0,0,memo)
        #print(memo)
        #print("---------------------------------")
        return sol
        
        