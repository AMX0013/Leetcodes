class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        # dp = {}

        # for num in nums:
        #     dp[num] = dp.get(num,0)+1

        # min_nums, max_nums = min(nums) , max(nums)
        # # re-empty
        # nums = []
         
        # # Count Sort for O(N)
        # for i in range( min_nums, max_nums+1):
        #     if i in dp.keys():
        #         while dp[i] >0:
        #             nums.append(i)
        #             dp[i] -=1
        # dp = None

        nums.sort()
        # Actual logic
        result = []
        

        for i in range(0,len(nums)-2,3):
            subRes = nums[i:i+3]
            if subRes[2]-subRes[0] <= k :
                result.append( nums[i:i+3] )
            else:
                return []
                
        return result


            

        