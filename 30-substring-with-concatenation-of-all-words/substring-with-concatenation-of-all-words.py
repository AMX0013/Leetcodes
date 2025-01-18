class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = set()
        subStrLen = len(words[0])
        allWords = Counter(words)
        trial = 0
        while trial < subStrLen:
            # print('trial',trial)
            trySet = copy.copy(allWords)
            l = trial
            r= l
            while r < len(s):
                # print(l)
                # print('init trySet', trySet)
                while(len(trySet)):
                    # populate trySet, 
                    tryWord = s[r:r+subStrLen]
                    if (tryWord in allWords) and (trySet[tryWord] >0 ):
                        trySet[tryWord] -= 1
                        r+=subStrLen
                        if trySet[tryWord] == 0:
                            del trySet[tryWord]
                    else:
                        l+=subStrLen
                        r=l
                        trySet = copy.copy(allWords)
                        break
                    # print(trySet)
                if len(trySet.keys()) == 0 :
                    # jackpot, 
                    
                    res.add(l)
                    # SLIDE
                    trySet[s[l:l+subStrLen]] = trySet.get(s[l:l+subStrLen], 0) +1
                    l+=subStrLen
            trial +=1
            
        return list(res)
        