class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s)+1)]

        dp[len(s)] = True
        

        for i in range(len(s)-1 ,-1, -1):
            
            for word in wordDict:               

                if i+len(word) <= len(s) :
                    # print(s[i:i+len(word)] ,"==", word , s[i:i+len(word)] == word)
                    # print("dp[",i,"+len(word) ",len(word),"] == True", dp[i+len(word)] )

                    if s[i:i+len(word)] == word and dp[i+len(word)] == True :
                    
                        dp[i] = True
                        # print(dp)
                        continue
        print(dp)
        return dp[0] 
