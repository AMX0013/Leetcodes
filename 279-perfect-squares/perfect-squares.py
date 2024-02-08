class Solution:
    def numSquares(self, n: int) -> int:
        sqrs = []
        j= 1

        while j*j <=n:
            sqrs.append(j*j)
            j+=1

        # sqrs = [i*i for i in range(1, int(n ** 0.5) + 1)][::-1]
        print(sqrs)

        q = deque()
        visited = set()
        q.append((n,0))

        while q:
            num, step  = q.popleft()

            if num == 0:
                # print()
                return step
            
            for sqr in sqrs:
                if num-sqr >=0 and num-sqr not in visited:
                    q.append( ( num-sqr, step+1  ))
                    visited.add(num-sqr)
        return 0

        # memo = []
        
        # if n ==0:
        #     return 0
        # j=0

        # while j <=n:
        #     memo.append(j)
        #     j+=1
        
        # x = 1
        # while x<= n:

        #     i = 1
        #     while i*i <=  x:
        #         memo[x] = min( memo[x], 1+memo[x-i*i])
        #         i+=1
        #     x+=1
        

        # return memo[n]