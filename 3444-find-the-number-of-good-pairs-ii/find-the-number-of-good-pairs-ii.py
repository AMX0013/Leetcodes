class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        countNums1 = Counter(nums1)  
        countNums2 = Counter(nums2) 
        limit = max(nums1) 
        multiplesCount = {}


        if k == 1 and nums2 == [1]*len(nums2):
            return len(nums2) * len(nums1)       

        for num2 , count2 in countNums2.items():
            multiple = num2 * k
            for multiple_value in range(multiple, limit + 1, multiple):
                if multiple_value in multiplesCount:
                    multiplesCount[multiple_value] += count2
                else:
                    multiplesCount[multiple_value] = count2
        
        res = 0
        for num1 in countNums1.keys() :
            if num1 in multiplesCount:
                res += countNums1[num1] * multiplesCount[num1]
                # print(num1, "countNums1[num1]",countNums1[num1],"multiplesCount[num1]",multiplesCount[num1], countNums1[num1] * multiplesCount[num1] )
                
#         print(multiplesCount)
#         print()
#         print(countNums1)
        return res
        
        