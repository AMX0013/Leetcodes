class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Tabulation method
        # either move t1 and check
        # or move t2 and check
        # or move both forward

        dp = [[0]*(len(text1)+1) for _ in range(len(text2)+1)]
        print(dp)


        for i in range(len(text2)):
            for j in range(len(text1)):
                dp[i+1][j+1] = ( 
                    (dp[i][j]+1) if text1[j] == text2[i]    #when the chars present in said indices are the same for the 2 strings, inc LCS by 1
                     else max(dp[i][j+1] , dp[i+1][j] )     #else max depicts best traversal of the 2 choices, increment index of i or j by 1 
                )

        return dp[-1][-1]