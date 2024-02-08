class Solution:
    def numSquares(self, n: int) -> int:
        memo = defaultdict()

        def psChec(num:int):
            
            if num ==0:
                return 0

            least = num
            if num in memo.keys():
                return memo[num]
            
            i = 1
            while i*i <=  num:
                least = min(least, 1+psChec(num-i*i))

                i+=1
            
            memo[num] = least
            return least

        return psChec(n)