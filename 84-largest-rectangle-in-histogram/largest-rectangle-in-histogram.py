class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = -1
        # Goal, maintain a monotonic stack with increasing or decreasing area

        # Simillar to daily temps, lets keep adding until the next day until when the area increases?
        # Technically this could be like kadane's ?

        for i, ht in enumerate(heights):
            # print('Gauging Tower of height', ht,'occuring at idx',i)
            startIdx = i
            while len(stack)> 0 and ht <= stack[-1][0]:
                poppedHt, poppedIdx = stack.pop() 
                # startidx recedes to go back to until when we must retroactively calc area
                # print('popped Tower of height', poppedHt,'occuring at idx',poppedIdx)
                # compute popped area, use  the pooped Ht, since, it is going to dec, more we pop
                # until we reach a point when the poppedHt is lt ht
                # use absolute i, since it is being modified
                area = max(area,  (poppedHt* (i - poppedIdx )) )
                # print('new max area = ', area,'b/w',startIdx, poppedIdx )
                # Crucial part, indicating from where this least common ht starts from, for the newly added ele
                startIdx = poppedIdx 
            # append currHt, showing which idx onwards is this the least common ht 
            stack.append((ht,startIdx))
        # Now leftovers,these are strictly increasing
        # these are areas that need to be evaluated, from their idx to len of the hrights arr
        for ht, idx in stack:
            area =max(area, (ht * (len(heights)-idx) ))
        # print(stack)
        return area
