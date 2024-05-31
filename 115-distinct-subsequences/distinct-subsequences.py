class Solution:

    def recur(self, s:str, t:str, s_idx:int, t_idx:int, dp)->int:

        

        if t_idx == len(t):
            # looks like we reached end of t, 
            # so backtrack and this is one valid answer
            return 1
        if s_idx == len(s):
            # reached end of string, return 0 as nothing found
            return 0

        # add memoization
        if dp[s_idx][t_idx] !=-1:
            return dp[s_idx][t_idx]

        # the result which holds when the choice of taking the element at s_idx
        pick = 0
        
        if s[s_idx] == t[t_idx]:
            # only if it matches with element at t_idx
            pick = self.recur(s,t,s_idx+1, t_idx+1, dp)
        # Now lets see what happens if we skip it
        skip = 0
        skip = self.recur(s,t,s_idx+1,t_idx, dp)

        dp[s_idx][t_idx] = pick + skip

        # return the result of the 2 moves. addition as it will back-propagate
        return dp[s_idx][t_idx]
    
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[-1 for _ in range( len(t))] for _ in range(len(s))]

        return self.recur(s,t,0,0, dp)