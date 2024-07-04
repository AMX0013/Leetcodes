class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in range(len(temperatures))]
        mono_dec_stack = []

        for idx, num in enumerate(temperatures):

            while  len(mono_dec_stack) >0 and mono_dec_stack[-1][0] < num:
                numm, indx =  mono_dec_stack.pop()
                res[indx] = idx-indx

            mono_dec_stack.append( (num, idx) )
        return res
            

        