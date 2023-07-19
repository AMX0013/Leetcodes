import math
class Solution:
    

         


    def maxSubArray(self, nums: List[int]) -> int:
        currSum = nums[0]
        globalMax = nums[0]
        for i in range(1, len(nums)):
            currSum = max(nums[i] , nums[i] + currSum )
            globalMax = max(globalMax, currSum)

        return globalMax
