class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in range(len(temperatures))]
        stack = [] # takes tuples, (temp, idx: the day when it i observed)
        for idx, temp in enumerate(temperatures):
            while len(stack) > 0 and temp > stack[-1][0] :
                idc_abt_temp_that_day, dayDate = stack.pop()
                res[dayDate] = idx - dayDate

            stack.append( (temp, idx) )

        return res


        