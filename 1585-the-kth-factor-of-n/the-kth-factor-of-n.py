import bisect

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        i=1
        resLow = []
        resHigh = []
        while i*i <= n:
            if n%i ==0:
                resLow.append(i)
                k-=1                
                if k==0:
                    return i
                if n//i != i:
                    resHigh.append(n//i)
            i+=1
        if k <= len(resHigh):
            return resHigh[-k]
        else:
            return -1
