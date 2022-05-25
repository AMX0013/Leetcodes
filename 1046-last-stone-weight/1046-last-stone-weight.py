import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = []
        for i in stones:
            heapq.heappush(minHeap,-1*i)
            
        while len(minHeap) >1 :
            y= -1*heapq.heappop(minHeap)
            x = -1*heapq.heappop(minHeap)
            
            if y == x:
                continue
            else:
                heapq.heappush(minHeap,-1*abs(y-x) )
                
        if len(minHeap) == 0:
            return 0
        else:
            return -1*minHeap[0]
            
        