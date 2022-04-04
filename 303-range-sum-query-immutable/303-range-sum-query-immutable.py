class NumArray:

    def __init__(self, nums: List[int]):
        
        self.prefixSum = [None for i in range(len(nums))]
        i=0
        if len(nums) > 0:
            self.prefixSum[0] = nums[0]
        if len(nums) >= 1:
            
            while i < len(nums)-1:
                i+=1
                print(i)
                self.prefixSum[i] =  self.prefixSum[i-1] + nums[i]
                
        
    def sumRange(self, left: int, right: int) -> int:
        if left ==0:
            return self.prefixSum[right]
        else: 
            return self.prefixSum[right] - self.prefixSum[left-1]
            
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)