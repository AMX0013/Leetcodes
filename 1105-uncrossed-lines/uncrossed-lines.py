class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        


        # +---+---+---+---+---+
        # |   |   | 1 | 4 | 2 |
        # +---+---+---+---+---+
        # |   | 0 | 0 | 0 | 0 |
        # +---+---+---+---+---+
        # | 1 | 0 | ^ |   |   |
        # +---+---+---+---+---+
        # | 2 |   |   |   |   |
        # +---+---+---+---+---+
        # | 4 |   |   |   |   |
        # +---+---+---+---+---+


        # convert this to 1D
       
        # | 0 | 0 | 0 | 0 |
        # +---+---+---+---+
        # | 0 | ^ |   |   |
        # +---+---+---+---+

        # nums2 is horizontal   (dp arrays) 
        # For DPs where we are looking backwards, lets keep that row clear
        prev = [0]*(len(nums2)+1)

        # nums1 flows vertical  



        # visualising prev & curr


        for i in range(len(nums1)):
            curr = [0]*(len(nums2)+1)
            for j in range(len(nums2)):

                if nums1[i] == nums2[j]:
                    curr[j+1] = 1 + prev[j]
                else:
                    # At curr[j+1] , we want the max value if 
                    curr[j+1] = max( curr[j] , prev[j+1] ) 
            
            prev = curr
        
        return curr[-1]
                



