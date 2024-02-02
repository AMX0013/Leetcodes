class Solution:
    def minDeletions(self, s: str) -> int:
        deletions = 0

        usedFreqSet = set()

        freqMap = Counter(s)

        for char, freq in freqMap.items():
            while freq>0 and freq in usedFreqSet:
                deletions +=1
                freq-=1
            usedFreqSet.add(freq)

        return deletions


