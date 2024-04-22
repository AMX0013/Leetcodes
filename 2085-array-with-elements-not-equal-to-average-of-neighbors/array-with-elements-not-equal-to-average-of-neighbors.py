class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        n = len(nums)
        res = [0]*n
        i = 0
        while i < n:
            res[i] = heapq.heappop(nums)
            i+=2
        i = 1
        while i < n:
            res[i] = heapq.heappop(nums)
            i+=2

        return res

        