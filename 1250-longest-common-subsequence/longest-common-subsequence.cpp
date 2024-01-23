class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        vector<vector<short>> dp(2, vector<short>(text1.size()+1, 0));

        for( short i = 0; i<text2.size();i++){
            for (short j = 0; j<text1.size(); j++){
                // if the chars match
                if (text2[i] == text1[j]){
                    dp[1][j+1] = dp[0][j]+1;
                }
                else{
                     dp[1][j+1] = max(dp[1][j] , dp[0][j+1]);
                }
            }
            dp[0] = dp[1];
        }
        return dp[1][text1.size()];
    }
};