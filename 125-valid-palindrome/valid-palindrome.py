class Solution:
    def isPalindrome(self, s: str) -> bool:
        def squish(text):
            return "".join(ch for ch in text if ch.isalnum())
        s = squish(s).lower()

        l = 0
        r = len(s)-1

        while l<=r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                return False
        return True
        
        