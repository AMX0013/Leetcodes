class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        size = len(nums)       

        dp = {}

        for num in nums:
            dp[num] = dp.get(num,0)+1

        print(dp)
        
        result = []

        subRes = [] 

        for i in range(min(nums) , max(nums)+1):
            if i in dp.keys():
                while dp[i] >0:
                    val = i
                    dp[i] -=1
                    print("Current subRes:", subRes, "val = ", val)
                    match len(subRes):
                        
                        case 2:
                            if val - subRes[0] <=k:
                                subRes.append(val)
                                result.append(subRes)
                                subRes = []
                            else:
                                return []
                                
                        case 1:
                            if val - subRes[0] <=k:
                                subRes.append(val)
                            else:
                                return []
                        case 0:
                            subRes.append(val)
                        case _:
                            return []
                            
                
        return result


            

        