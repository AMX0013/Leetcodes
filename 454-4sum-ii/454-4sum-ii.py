class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        
        hashMap = defaultdict(int)
        
        res=0
        
        for i in range(n):
            for j in range(n):
                hashMap[nums1[i] + nums2[j] ]+=1
            
        for x in range(n):
            for y in range(n):
                res += hashMap[ -1* (nums3[x]+nums4[y]) ]
        
        return res
        