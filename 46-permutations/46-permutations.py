class Solution:
    def __init__(self):
        self.res=[]
   
    def backTrack(self, nums, path): #
        #Ending condition >>
        if not nums:
            # if nums is empty from slicing out , end it
            self.res.append(path)
        for x in range(len(nums)):
            self.backTrack(nums[:x]+nums[x+1:] ,path+[nums[x]])
            
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.backTrack(nums,[])
        return self.res
        