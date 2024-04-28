class Solution:
    def isPali(self,word):
        return word == word[::-1]
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.isPali(word):
                return word
        return ""

        
        