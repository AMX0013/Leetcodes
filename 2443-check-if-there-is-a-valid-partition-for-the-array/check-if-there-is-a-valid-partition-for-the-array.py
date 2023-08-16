class Solution:
    def validPartition(self, nums: List[int]) -> bool:

        # A valid partition exists if one of these are true

        # The subarray consists of exactly 2 equal elements. For example, the subarray [2,2] is good.

        # The subarray consists of exactly 3 equal elements. For example, the subarray [4,4,4] is good.

        # The subarray consists of exactly 3 consecutive increasing elements, that is, 
        # the difference between adjacent elements is 1. 
        #     For example, the subarray [3,4,5] is good, but the subarray [1,3,5] is not.

        # Return true if the array has at least one valid partition. Otherwise, return false.

        # The partitioned subarrays are all supposed to be evaluated, and not just if one subarray succeeds!

        n = len(nums)

        memo = {}
        memo[n] = False

        def recur(i):
            
            if i == n:
                memo[i] = True
                return True
            if i in memo.keys():
                return memo[i]
            res = False

            if i+1<n and nums[i]==nums[i+1]  :
                res =  recur(i+2)
            if i+2<n :
                if  nums[i]==nums[i+1]==nums[i+2] or nums[i]==nums[i+1]-1==nums[i+2]-2 :
                    res = res or recur(i+3)

            # print(i,memo)
            memo[i]= res
            return res
        
        res = recur(0)

        # print(memo)


        return memo[n]
