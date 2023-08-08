class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:

        # The idea is to start from the back
        # Since starting from front will cause us to grow and then start from 0 again
        # Caused due to the fact that a bigger number ahead will cause us to stop and start from what we have built

        #  in the case of a strictly decreasing monotonic stack, its gonna be the first element
        maximise = nums[0]

        for i in range(len(nums)-1,0,-1):
            if nums[i-1] <= nums[i]:
                nums[i-1]+= nums[i]
                maximise = max(maximise,nums[i-1])
        print(nums)
        return maximise

