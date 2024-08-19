class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # Find all factors of n
        count = 0
        # all factors should be from 1 to sqrt(n)
        for i in range(1,n+1):
            if n%i==0:
                count +=1
                # res = i
                if count == k:
                    return i
                # res.add( n//i )
        return -1

        
        