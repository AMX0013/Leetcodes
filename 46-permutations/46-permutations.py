class Solution:
    '''
    def __init__(self):
        self.res=[]
   
    def backTrack(self, nums, path): #
        #Ending condition >>
        if not nums:
            # if nums is empty from slicing out , end it
            self.res.append(path)
        for x in range(len(nums)):
            self.backTrack(nums[:x]+nums[x+1:] ,path+[nums[x]])
        
    '''
      
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''        
        self.backTrack(nums,[])
        return self.res
        
        '''
        
        result = [] # not defined globally to prevent addition of sub level call stack permutations
        
        # base case
        
        if len(nums) == 1:
            return [nums[:]] #return copy of the array containing a single elemnt
        
        # for [1,2,3] > 
        #print(">",nums)
        for i in range(len(nums)) : # note> this runs for len(nums) times to prvent the final shuffle to come back to the original one, in order to prevent duplicate permutations
            #print("level ",len(nums),"item = ",nums[i])
            n = nums.pop(0) # holds the first element > to process permustations of the rest
            perms = self.permute(nums)
            #print("no of permutations:",len(perms))
            #print(perms)
            for aPermutaion in perms:
                aPermutaion.append(n)  # so for [1,2,3] > n=1 , perms = [  [2,3] , [3,2] ]
            #resulting perms = [ [2,3,1] , [3,2,1] ]
            #print("final res",perms)
            result.extend(perms) # perms will always end up complete
            
            
            # so, as we popped 1 into n initially, we shuffle the number and turn it to 231  now
            nums.append(n)
        return result
            
            
            
        