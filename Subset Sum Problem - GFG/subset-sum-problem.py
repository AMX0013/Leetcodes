#User function Template for python3

class Solution:
    def __init__(self):
        self.res = [] 
    def isSubsetSum (self, N, arr, sum):
        # code here 
        S = [[False for _ in range(sum+1) ] for _ in range(len(arr)+1) ]


        for i in range(len(arr)+1):
            S[i][0] = True
        

        for i in range(1,len(arr)+1):
            for j in range(1,sum+1):
                if  j < arr[i-1]:
                    S[i][j] = S[i-1][j]
                else:
                    S[i][j] = S[i-1][j] or S[i-1][j-arr[i-1]]
        
        return bool(S[len(arr)][sum])
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)
            
        

# } Driver Code Ends