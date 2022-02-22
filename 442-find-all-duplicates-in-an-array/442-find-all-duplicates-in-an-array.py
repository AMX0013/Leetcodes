class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq= {}
        res = []
        for i in range(1,n+1):
            freq[i] = 0
        print(freq)   
        
        for x in range(0,len(nums) ):
            print(x,nums[x])
            freq[nums[x]] += 1
            
        for j in freq:
            if freq[j] == 2:
                res.append(j)
        return res