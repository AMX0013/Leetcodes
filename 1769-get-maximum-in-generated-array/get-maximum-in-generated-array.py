class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0 for _ in range(n+1)]
        if n==0:
            return 0
        nums[1] = 1
        i=0
        maxRes = 0
        while 2*i < n+1:
            nums[2*i] = nums[i]
            maxRes = max(maxRes,nums[2*i])

            if 2*i+1<n+1:
                nums[2*i+1] = nums[i]+ nums[i+1]
                maxRes = max(maxRes,nums[2*i+1])

            i+=1
        print(nums)
        return maxRes
