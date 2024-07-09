from collections import deque

class Solution:    
    def findTheWinner(self, n: int, k: int) -> int:
        # start = 0
        # q = deque([x for x in range(1,n+1)])
        # # print(q)
        '''
        1: A deque to rotate the list keeping our pointer stationary
        '''
        # for siz in range(n,1,-1):

        #     for _ in range(k):
        #         temp = q.popleft()
        #         q.append(temp)
        #     q.pop()
        #     # print(q)

        
        # return q[0]
        '''
        2:, based on neetcode's explanation, we expland deque solution with prints
        and track how the position of our result varied. with values of n for given k
        '''
        def solver(n,k):
            if n ==1:
                return 0
            # res is at loc (prev_res +k) % curr_size: n
            return (solver(n-1,k) + k) % n
        return solver(n,k)+1
        
        '''
        3> Unwrap 2, with a bottom up only. 
        '''
        res = 0

        for curr_size in range(n+1,1,-1):
            res += (res+k) % curr_size

        return res+1


        