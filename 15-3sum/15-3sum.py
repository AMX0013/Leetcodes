class Solution:
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        #print(nums)
        res = []
        for num1x in range(len(nums)-2):
            if num1x >0 and nums[num1x] == nums[num1x-1]:
                continue
            
            num2x = num1x+1
            num3x = len(nums)-1
            #print(nums[num1x] , nums[num2x], nums[num3x])
            while num2x < num3x:
                 
                sumX = nums[num1x] + nums[num2x] + nums[num3x]
                if  sumX ==0:
                    res.append([ nums[num1x] , nums[num2x], nums[num3x] ])
                    #print("sol obtained",nums[num1x] , nums[num2x], nums[num3x])
                    num2x+=1
                    while nums[num2x] == nums[num2x-1] and num2x < num3x :
                        print(num2x)
                        num2x+=1
                    num3x -=1
                    while nums[num3x] == nums[num3x+1] and num2x < num3x :
                        #print(num3x)
                        num3x -= 1
                elif sumX >0:
                    
                    num3x -= 1
                    #print("<",nums[num3x])
                else:
                    num2x+=1
                    #print(">",num2x)
            #num1x+=1
        #print(res)        
        return res
            
            
        