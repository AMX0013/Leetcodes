import math

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # words 10**4
        # words[i] 30, compute on this

        # set lookup is O(1)
        wordset = set(words)
        # require a space to store results
        res = []
        memo = {}

        dp = {}
        output = []
        def recur(word: str):
            # if word
            # print("exploring word: ", word)
            if word in dp:    
                # print("Precomputed for ",word)            
                return dp[word]
            '''
            # def check(prefix: string, suffix: string):
            #     if (prefix in wordset ):
            #         combo = [prefix]
            #         if (suffix in wordset) :
            #             combo.append(suffix)
            #             print("Found combo!",combo, "for word: ",word)
            #             memo[word] = memo.get(word, [])
            #             memo[word].append(combo)
            #             return True

            #         if (recur(suffix)) :
            #             for combinations in memo[suffix]:
            #                 combo.extend(combinations)   

            #                 print("Found combo!",combo, "for word: ",word)
            #                 memo[word] = memo.get(word, [])
            #                 memo[word].append(combo)
            #                 return True
            #     else:
            #         print("dropped",prefix,suffix)
            '''
            for i in range(1,len(word)):
                prefix = word[:i]
                suffix = word[i:]
                # returnVal = returnVal or check(prefix, suffix):
                # return returnVal
                if (prefix in wordset and suffix in wordset) or (prefix in wordset and recur(suffix)):
                    dp[word] = True
                    return True
                # must save the mf falses as well
            dp[word] = False
            return False
            # return returnVal

            
        for word in words:
            # memo[word] = list()
            # print("Checking combos for : ",word)
            if recur(word) :
                output.append(word)

        print(memo)
        # for key in output:
        #     res.append(memo[key][0])
        # print(res)
        return output