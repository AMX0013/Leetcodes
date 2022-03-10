class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        hashMap = {}
        for element in nums:
            hashMap[element]=0
        for element in nums:
            hashMap[element] += 1
        print(hashMap)    
        output = []
        
        for element in hashMap:
            print(element, hashMap[element])
            if hashMap[element] == 1:
                output.append(element)
        return output
        