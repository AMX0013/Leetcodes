class Solution:
    def validPartition(self, nums: List[int]) -> bool:

      
        n = len(nums)
        
        twoChoice = (nums[-1] == nums[-2])

        if len(nums)==2:
            return twoChoice
        
        threeChoice = ( (nums[-3] == nums[-2]-1 == nums[-1]-2) or (nums[-3] == nums[-2] == nums[-1]) )

        # Assume input [4,5,6]

        dp = [threeChoice , twoChoice, False]

        for i in range(n-4 , -1, -1):
            # at -4 :
                #  list = [4,4,5,6]
            # This choice says take [4,4] , [5,6] which is stored in two
            cur = (nums[i] == nums[i+1]) and dp[1]
            # at -5
                #  list = [4,4,4,5,6]
            # This choice says take [4,4] , [4,5,6] which is stored in three
            cur = cur or (

                (nums[i]==nums[i+1]==nums[i+2] or
                nums[i]==nums[i+1]-1==nums[i+2]-2) and
                dp[2]

            )
            # Think of this as a sliding window

            # shift dp contents to right by 1 and push in new val
            dp = [cur,dp[0],dp[1]]


        return dp[0]






        # # we only require 4 pos memory to store the results of each subarray that can exist
        # dp = [False for _ in range(3)]
        # # init last value to True 
        # dp[-1] = True

        # for i in range(n-2,-1,-1):
        #     print("i = ",i)
        #     res = False
        #     if i+1<n and nums[i]==nums[i+1]  :
        #         print("n%(i+2)",n%(i+2))
        #         if dp[n%(i+2)] == True:
        #             two = True
        #     if i+2<n :
        #         if  nums[i]==nums[i+1]==nums[i+2] or nums[i]==nums[i+1]-1==nums[i+2]-2 :
        #             print(n%(i+3))
        #             if dp[n%(i+3)] == True:
        #                 three = two or True
        #     dp = dp[three , two , ] 
        #     print(dp)

        







































        # memo = {}
        # memo[n] = False

        # def recur(i):
            
        #     if i == n:
        #         memo[i] = True
        #         return True
        #     if i in memo.keys():
        #         return memo[i]
        #     res = False

        #     if i+1<n and nums[i]==nums[i+1]  :
        #         res =  recur(i+2)
        #     if i+2<n :
        #         if  nums[i]==nums[i+1]==nums[i+2] or nums[i]==nums[i+1]-1==nums[i+2]-2 :
        #             res = res or recur(i+3)

        #     # print(i,memo)
        #     memo[i]= res
        #     return res
        
        # res = recur(0)

        # # print(memo)


        # return memo[n]
