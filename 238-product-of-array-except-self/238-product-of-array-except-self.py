class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [ 0 for x in range(len(nums))]
        print(res)
        zeroesCount = 0
         
        wholeProduct = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroesCount+=1
                zeroIndex = i
                if zeroesCount > 1:
                    return res
                continue
            
            wholeProduct *= nums[i]
            
        
        if zeroesCount == 1:
            res[zeroIndex] = wholeProduct
            return res
        
        for j in range(len(nums)):
            res[j] = wholeProduct // nums[j]
        
        return res