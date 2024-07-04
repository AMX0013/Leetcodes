class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        if denominator == 0:
            return ""
        
        res = ""
        # prep for negative on one of the numbers
        # XOR only
        
        if (numerator * denominator )< 0 :
            res += "-"
        
        num, den = abs(numerator), abs(denominator)

        quotient = str(num // den)

        res += quotient

        remainder = num % den
        if remainder == 0:
            return res
        res += '.'

        # process the real thing

        remainder_map = {}
        '''
            key: The remainder itself. for eg: 4/5, remainder = 4.
            value: len of the res string before we add the remainder to it
        '''


        # the whole recurring decimal will be generated and stored as remainder
        while remainder != 0 and remainder not in remainder_map:
            print(remainder, remainder_map)

            # add len(res) of curr iter to state index loc of remainder
            remainder_map[remainder] = len(res)
            # print(remainder_map)
            # literally how u do 4/5 remainder calc
            remainder *= 10
            res += str(remainder // den)
            # the next amounts to be processed
            remainder %= den

            

        # check for repeats
        if remainder in remainder_map:
            
            res = res[:remainder_map[remainder]] + "("  + res[remainder_map[remainder]  : ] + ")"
            
            # print(res)
        return res




        
        