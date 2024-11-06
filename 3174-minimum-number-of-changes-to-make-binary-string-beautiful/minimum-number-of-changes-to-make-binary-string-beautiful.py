class Solution:
    def minChanges(self, s: str) -> int:
        edits = 0
        i = 0
        lenth = len(s)
        while i < lenth:
            if s[i] != s[i+1]:
                edits+=1
            i+=2
        return edits
        