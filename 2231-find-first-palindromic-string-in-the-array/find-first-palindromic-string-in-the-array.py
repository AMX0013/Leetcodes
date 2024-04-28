class Solution:
    def isPali(self,word):
        n = len(word)
        i=0
        j=n-1
        while i<=j:
            if word[i] != word[j]:
                return False
            i+=1
            j-=1
        return True
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.isPali(word):
                return word
        return ""

        
        