class Solution:
    def minDeletions(self, s: str) -> int:
        deletions = 0
        usedFreq = set()
        # for each unique character
        for char in set(s):
            # count
            freq_underCalculation = s.count(char)
            while freq_underCalculation > 0 and freq_underCalculation in usedFreq:
                freq_underCalculation -=1
                deletions+=1
            usedFreq.add(freq_underCalculation)

        return deletions


