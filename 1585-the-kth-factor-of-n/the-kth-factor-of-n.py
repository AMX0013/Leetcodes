class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # Find all factors of n
        res = set()
        # all factors should be from 1 to sqrt(n)
        for i in range(1,int(sqrt(n))+1 ):
            if n%i==0:
                res.add(i)
                res.add( n//i )
        # print(res)
        num = -1
        if len(res) < k:
            return num
        # in a sorted list of all factors of n,
        res = list(res)
        heapify(res)
        # print(res)
        
        
        for _ in range(k):
            num = heapq.heappop(res)

        return num
        # return the kth index elemnt
        