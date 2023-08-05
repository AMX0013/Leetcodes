class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp=[[False,[""]] for _ in range(len(s)+1)]
        dp[len(s)]=[True,[""]]

        for i in range(len(s)-1,-1,-1):
            retArr = []
            retValBool = False
            for word in wordDict:
                if i+len(word) <= len(s):


                    if s[i:i+len(word)] == word and dp[i+len(word)][0] == True:

                        print(i,s[i:i+len(word)],dp[i+len(word)][1])

                        retValBool = True
                        prevArrs = dp[i+len(word)][1]
                        
                        for chars in prevArrs:
                            # print(word)
                            if chars == "":
                                chars = word + chars
                            else:
                                chars = word + " " + chars
                            
                            chars.rstrip()
                            retArr.append(chars)
                            
            print(retArr)
            
            dp[i][0] = retValBool
            dp[i][1] = retArr
        
        print(dp)
        res = dp[0][1]
        
        return res