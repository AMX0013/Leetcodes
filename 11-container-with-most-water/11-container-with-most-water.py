import heapq
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxDiff = -1
        maxHeight = -1
        maxWater = 0
        LCHeight = -1
        i = 0
        j = len(height)-1
        height1 = height[i]
        height2 = height[j]
        
        while i < j:  
            dist = j-i
            if height[i] <= height[j]:
                water = height[i]* dist
                i+=1
            else:
                water = height[j]* dist
                j-=1
            if water > maxWater:
                maxWater = water
                       
        return maxWater