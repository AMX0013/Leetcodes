from collections import deque

class Solution:    
    def findTheWinner(self, n: int, k: int) -> int:
        start = 0
        q = deque([x for x in range(1,n+1)])
        # print(q)

        for siz in range(n,1,-1):

            for _ in range(k):
                temp = q.popleft()
                q.append(temp)
            q.pop()
            # print(q)

        
        return q[0]

        