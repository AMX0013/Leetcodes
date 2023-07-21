class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqMapS = defaultdict()

        freqMapT = defaultdict()

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            freqMapS[s[i]] = freqMapS.get(s[i],0)+1
            freqMapT[t[i]] = freqMapT.get(t[i],0)+1

        print(freqMapS  )

        for key in freqMapS.keys():
            if key in freqMapT.keys():

                if freqMapS[key] != freqMapT[key]:
                    return False
            else:
                return False
        return True