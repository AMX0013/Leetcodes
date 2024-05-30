class Solution:
    def numSteps(self, s: str) -> int:
        n = len(s)
        carry = 0
        steps = 0

        for i in range(n-1,0,-1):
            # a carry bit will be set when we add 1 with 1, to yield 0. 
            # carry bit stays on an outlasts everything . we iterate just until the leftmost bit
            if carry + int(s[i]) == 1:
                steps += 2
                carry = 1
            else:
                steps+=1
        # at the leftmost bit, if carry is set, then 1 extra step, as carry basically means x2
        if carry == 1:
            steps+=1
        
        return steps