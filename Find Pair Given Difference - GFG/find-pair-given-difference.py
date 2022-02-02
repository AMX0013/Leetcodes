#User function Template for python3

class Solution:

    def findPair(self, arr, L,N):
        arr.sort()
        for index in range(L):
            res = arr[index] + N
            if self.binarySearch(arr, index+1,L-1,res):
                return True
        return False
        #code here
    def binarySearch(self, arr, Left, Right ,N):
        
        while Left <= Right:
            mid = (Left + Right)//2
            if N== arr[mid]:
                return True
            elif N < arr[mid]:
                Right = mid-1
            elif N > arr[mid]:
                Left = mid+1
        return False
            
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        L,N = [int(x) for x in input().split()]
        arr = [int(x) for x in input().split()]

        solObj = Solution()

        if(solObj.findPair(arr,L, N)):
            print(1)
        else:
            print(-1)
# } Driver Code Ends