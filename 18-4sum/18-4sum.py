class Solution:
    def recursiveSum(self,nums,target,setSize,startLoc):
        if setSize ==2:
            ################################## base case = two sum #####################################
            res = []
            num2x = startLoc +1
            num3x = len(nums)-1
            while num2x < num3x:
                 
                sumX = nums[num2x] + nums[num3x]
                if  sumX == target:
                    res.append([ nums[num2x], nums[num3x] ])
                    #print("sol obtained",nums[num1x] , nums[num2x], nums[num3x])
                    num2x+=1
                    while nums[num2x] == nums[num2x-1] and num2x < num3x :
                        print(num2x)
                        num2x+=1
                    num3x -=1
                    while nums[num3x] == nums[num3x+1] and num2x < num3x :
                        #print(num3x)
                        num3x -= 1
                elif sumX > target:
                    
                    num3x -= 1
                    #print("<",nums[num3x])
                else:
                    num2x+=1
            return res
            ##############################################################################################
        else:
            
            for i in range(startLoc,len(nums)-setSize-1):
                if i>0 and nums[i]==nums[i-1]:
                    continue
                curr = nums[i]
                temp = []
                res = []
                total = []
                print("====>",curr,setSize,">",target)
                temp = self.recursiveSum(nums,target-curr,setSize-1,startLoc+1)
                if temp:
                    for j in range(len(temp)):
                        
                        tempSet = []
                        tempSet.append(curr)
                        for k in range(len(temp[0])):

                            tempSet.append(temp[j][k])
                        res.append(tempSet)


                    print(res)
                total.append(res)
                
            return total

            
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        nums.sort()
        res = []
        res = self.recursiveSum(nums,target,4,0)
        return res
        '''
        
        nums.sort()
        #print(nums)
        res = []
        
        for num0x in range(len(nums)-3):
            '''if num0x >0 and nums[num0x] == nums[num0x-1]:
                    continue'''
            #print("====>",num0x)
            for num1x in range(num0x+1,len(nums)-2):
                '''if num1x >1 and nums[num1x] == nums[num1x-1] :
                    continue'''
                #print("===>",num1x)
                num2x = num1x+1
                num3x = len(nums)-1
                #print(nums[num1x] , nums[num2x], nums[num3x])
                while num2x < num3x:

                    sumX = nums[num0x]+ nums[num1x] + nums[num2x] + nums[num3x]
                    if  sumX == target:
                        tempRes = [ nums[num0x],nums[num1x] , nums[num2x], nums[num3x] ]
                        if tempRes not in res:
                            res.append(tempRes)
                            #print("sol obtained",nums[num1x] , nums[num2x], nums[num3x])
                        num2x+=1
                        while nums[num2x] == nums[num2x-1] and num2x < num3x :
                            #print(num2x)
                            num2x+=1
                        num3x -=1
                        while nums[num3x] == nums[num3x+1] and num2x < num3x :
                            #print(num3x)
                            num3x -= 1
                    elif sumX > target:

                        num3x -= 1
                        #print("<",nums[num3x])
                    else:
                        num2x+=1
                        #print(">",num2x)

            
        #print(res)        
        return res
        
        