class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        # O(m*n)
        memo = {}

        # O(m*n) TC Unique computations
        def recurLCS(i,j):


            # Termination Condition:

            if i == len(nums1) or j == len(nums2):
                return 0
            # return cached val
            if (i,j) in memo:
                return memo[(i,j)]

            if nums1[i] == nums2[j]:
                # Cache current value:
                memo[(i,j)] = 1 + recurLCS(i+1,j+1)

                return memo[(i,j)]

            else:
                # This enforces that they only move in one direction 
                    # Basically no crosses, as we dont go to thier respective preceding values 
                memo[(i,j)] = max( recurLCS(i+1,j) , recurLCS(i,j+1))

                return memo[(i,j)]

        return recurLCS(0,0)
