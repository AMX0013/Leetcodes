class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = set()
        subStrLen = len(words[0])
        allWords = Counter(words)
        trySet = Counter()
        trial = 0
        while trial < subStrLen:
            # print('trial',trial)
            l = trial
            r= l
            while r < len(s):
                # print(l)
                # print('init trySet', trySet)
                while(trySet != allWords):
                    # populate trySet, 
                    tryWord = s[r:r+subStrLen]
                    if (tryWord in allWords) and (trySet[tryWord] < allWords[tryWord] ):
                        trySet[tryWord] += 1
                        r+=subStrLen
                    else:
                        l+=subStrLen
                        r=l
                        trySet = Counter()
                        break
                    # print(trySet)
                if trySet== allWords:
                    # jackpot, 
                    
                    res.add(l)
                    # SLIDE
                    trySet[s[l:l+subStrLen]] -=1
                    l+=subStrLen
            trial +=1
            trySet = Counter()
        return list(res)
        