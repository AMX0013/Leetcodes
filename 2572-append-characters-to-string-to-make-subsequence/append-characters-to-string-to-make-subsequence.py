class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t_idx = 0

        for i in range(len(s)):

            if s[i] == t[t_idx]:
                # print("match s[i]", s[i], "and t[", t_idx, "] : " ,t[t_idx] )
                t_idx+=1
                
            if t_idx == len(t) :
                return 0
            
        return len(t) - (t_idx)
