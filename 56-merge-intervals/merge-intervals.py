class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        # print(intervals)
        i=0
        while(i < len(intervals)-1):
            if intervals[i][1] >= intervals[i+1][0] :
                r = max(intervals[i][1], intervals[i+1][1])
                # merge the two intervals 
                mergedInterval = [intervals[i][0], r]
                # and store
                intervals.pop(i)
                intervals[i] = mergedInterval
                # print('Intervals after merging:',intervals)
            else:
                i+=1
            # print(i)
        return intervals
        