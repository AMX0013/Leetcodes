class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        for i in range(1,len(nums)-1):
            if nums[i-1] < nums[i] < nums[i+1] or  nums[i-1] > nums[i] > nums[i+1]:
                nums[i] , nums[i+1] = nums[i+1], nums[i]
        return nums

        # heapq.heapify(nums)
        # n = len(nums)
        # res = [0]*n
        # i = 0
        # while i < n:
        #     res[i] = heapq.heappop(nums)
        #     i+=2
        # i = 1
        # while i < n:
        #     res[i] = heapq.heappop(nums)
        #     i+=2

        # return res

        