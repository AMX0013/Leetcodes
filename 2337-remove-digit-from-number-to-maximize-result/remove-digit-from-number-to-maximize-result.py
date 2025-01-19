class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        res = []
        for i in range(len(number)):
            if number[i] == digit:
                res.append( int(number[:i] + number[i+1:]) )
        return str(max(res))
        