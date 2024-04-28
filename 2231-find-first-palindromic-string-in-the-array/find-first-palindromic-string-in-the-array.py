class Solution:
    # def isPali(self,word):
    #     return word == word[::-1]
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""

        
        