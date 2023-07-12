import math
class Solution:

    def destroyTargets(self, nums: List[int], space: int) -> int:

        # # nums[anchor] == nums[roamer] + c * space
        #                 # a + (n-1)*d ?

        # we dont care about (n) , and we have d, thus nums% space will yeild the same mf "a"  
        # Lets leverage that ploy and find basically largest seq, and from which we find our earliest starting element

        ApexList = []
        maxKills = 0
        dp = defaultdict( lambda : [0 , float(math.inf)])
        predA = 0 
        # nums.sort()
        for anchor in range(len(nums)):
            a = nums[anchor]% space
            # print("+++++++++++" , nums[anchor] , ">",a,"+++++++")
            # Need a datastructure where a is key, and value is
                # 1> The number of elemnts with the same a
                # 2> The minimum of all anchors that yield the same "a"
            dp[a][0] +=1

            

            dp[a][1] = min( dp[a][1] , nums[anchor] )
            
            # print(dp[a])

            if dp[a][0] > maxKills:
                maxKills = dp[a][0]
                
                ApexList = []
                ApexList.append(dp[a][1])
            if dp[a][0] == maxKills:
                ApexList.append(dp[a][1])



        # print(dp)
        return min(ApexList)







