class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]

        for i in range(1,len(intervals)):
            left = res[-1]
            right = intervals[i]
            if left[1] >= right[0]:
                res[-1] = [left[0], max(left[1], right[1])]
            else:
                res.append(right)
        return res