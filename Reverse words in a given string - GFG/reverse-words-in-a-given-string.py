
# User function Template for python3


class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        # code here 
        res = []
        arr = S.split(".") # delimiter is . here
        n = len(arr)
        for item in arr:
            n= n-1
            res.append(arr[n])
        l = (".".join(res))
        return l
#{ 
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))
# } Driver Code Ends