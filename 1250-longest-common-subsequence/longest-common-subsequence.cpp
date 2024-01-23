class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        vector<vector<short>> dp(text2.size()+1, vector<short>(text1.size()+1, 0));

        for( short i = 0; i<text2.size();i++){
            for (short j = 0; j<text1.size(); j++){
                // if the chars match
                if (text2[i] == text1[j]){
                    dp[i+1][j+1] = dp[i][j]+1;
                }
                else{
                     dp[i+1][j+1] = max(dp[i+1][j] , dp[i][j+1]);
                }
            }
        }
        return dp[text2.size()][text1.size()];
    }
};