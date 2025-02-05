class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 1D dp
        # funny words, u must reach idx len, while last idx of arr is len-1
        dp = deque()
        
        dp.append(cost[-1])
        dp.append(0)
        print(dp)
        for i in range(len(cost)-2,-1,-1):
            # len shall always be 2 only
            # no heap bs needed so far
            pay = cost[i] + min(dp)
            dp.pop()
            dp.appendleft(pay)
            # print('post',i,'need to pay', pay, 'dp:',dp)
        return min(dp)