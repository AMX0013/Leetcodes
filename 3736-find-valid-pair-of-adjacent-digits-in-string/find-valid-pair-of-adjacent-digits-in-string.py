class Solution:
    def findValidPair(self, s: str) -> str:
        freqMap = Counter(s)
        # print(freqMap)
        # need top find pair, from freqMap
        validNums = set()
        for key, val in freqMap.items():
            if int(key) == val:
                validNums.add(key)
        # print(validNums)
        # need to fiund when the elements are together
        for i in range(len(s)-1):
            if s[i] in validNums and s[i+1] in validNums and s[i]!= s[i+1]:
                return s[i:i+2]
        return ''


        