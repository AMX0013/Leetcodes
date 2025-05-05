class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        minI = [-10**9]*len(nums)
        minI[0] = nums[0]
        peakJstack = []
        k=1
        # Finding a j or a k even
        while k < len(nums):
            minI[k] = min(minI[k-1],nums[k])
            # if minI[k] == nums[k]:   useless, migh be used as new summit /\/\ but cannn aslo be skipped i think
            #     continue 
            while len(peakJstack) > 0 and nums[k] >= peakJstack[-1][0]:  #peak is not the one in range, should be monotonically decreasing?
                peakJstack.pop()
            # At the closest acttual summit J 
            if peakJstack and nums[k] > peakJstack[-1][1]:
                # print(peakJstack[-1][1], peakJstack[-1], nums[k], k)
                return True

            peakJstack.append((nums[k], minI[k]))  #new smaller summit
            # print(k, peakJstack)
            k+=1
        return False

        