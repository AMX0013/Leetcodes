import heapq
class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.kth = k
        for i in range(len(nums)):
            heapq.heappush(self.heap,nums[i])
            
        while len(self.heap)>self.kth:
            heapq.heappop(self.heap)
            
            
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap ,val)
        while len(self.heap)>self.kth:
            heapq.heappop(self.heap)
        #print(self.heap,"val = ",val)
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)