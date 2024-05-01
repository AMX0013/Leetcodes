import heapq # a minheap only
class MedianFinder:


    def __init__(self):
        # max heap to store the lower left number 
        # so that pop operation will yield the rightmost lowerend number
        # odd numbers? always get your median from here
        self.leftHalf_negMax = []
        # min heap to store the higher size number with a negative sign
        # so that pop operation will yield the leftmost higherend number

        self.rightHalf_posMin = []

    def addNum(self, num: int) -> None:
        # add number into a heap that will be popped and populate the main heap
            # the left size in our case
            # this ensures that the input is always sorted
        heapq.heappush(self.rightHalf_posMin, -(heapq.heappushpop(self.leftHalf_negMax, -num) ))
        
        # length of left half should always be larger and thus median will be here
        if len(self.leftHalf_negMax) < len(self.rightHalf_posMin):
            num =heapq.heappop(self.rightHalf_posMin)
            # push into leftHalf_negMax
            heapq.heappush(self.leftHalf_negMax, -num)
        # print("after add self.rightHalf_posMin:", self.rightHalf_posMin )
        # print("after add self.leftHalf_negMax:", self.leftHalf_negMax )

    def findMedian(self) -> float:
        if len(self.rightHalf_posMin) == len(self.leftHalf_negMax):
            R_pos_num =self.rightHalf_posMin[0]
            L_neg_num= self.leftHalf_negMax[0]
            res = (-L_neg_num + R_pos_num )/2  
            print("even res =", res)          
        else:
            # choose the lesser length heap and pop that        
            L_neg_num= self.leftHalf_negMax[0]
            res = -L_neg_num    
            print("median", res)
        return res
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()