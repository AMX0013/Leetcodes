class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        resLIS = []

        resLIS.append(nums[0])

        for i in range(1,len(nums)):

            if nums[i] > resLIS[-1]:
                resLIS.append(nums[i])
            else:
                mid = bisect_left(resLIS,nums[i])
                resLIS[mid] = nums[i]
        return len(resLIS)