class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        l=0
        r=0

        while l<=r and r<len(s):
            if r-l + 1 == k:
                if (r+1< len(s) and s[r+1] == s[r]) or (l-1 >=0 and s[l-1]== s[l]) :
                    r+=1
                    l=r
                    continue
                return True
            if r+1< len(s) and s[r+1] == s[r]:
                r+=1
            else:
                r+=1
                l=r
        return False
        