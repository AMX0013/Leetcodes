class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        freq1 = {}
        freq2 = {}
        
        for j in nums:
            freq1[j] = 0
        for i in range(len(nums)+1):
            freq2[i] = 0
        for key in freq2:
            if key not in freq1:
                return key