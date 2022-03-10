class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        hashMap = {}
        for element in nums:
            hashMap[element]=0
        for element in nums:
            hashMap[element] += 1
        print(hashMap)    
        output = 0
        
        for element in hashMap:
            print(element, hashMap[element])
            if hashMap[element] == 1:
                output = element
        return output
        