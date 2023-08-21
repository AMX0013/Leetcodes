class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        N = len(s)

        for i in range(1,N//2 +1): #(n//2)+1 is max length of a feasible, repeatable substring
            # Intuition: The substring length is a factor of the whole string length

            if N % i == 0:
                sub = s[:i]

                if sub*(N//i) == s:
                    return True
        return False
