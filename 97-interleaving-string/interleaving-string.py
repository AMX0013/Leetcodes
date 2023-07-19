class Solution:

    '''
            This recursion goes all in and backtracks

            Goal string : aadbbcbcac

             +---+---+---+---+---+---+
            |   | d | b | b | c |   |
            +---+---+---+---+---+---+
            | a |   |   |   |   |   |
            +---+---+---+---+---+---+
            | a |   |   |   |   |   |
            +---+---+---+---+---+---+
            | b |   |   |   |   |   |
            +---+---+---+---+---+---+
            | c |   |   |   |   |   |
            +---+---+---+---+---+---+
            | c |   |   |   |   |   |
            +---+---+---+---+---+---+
            |   |   |   |   |   | T |
            +---+---+---+---+---+---+


    '''
    
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def topDownBacktrack(i,j):
            # Bottom Up approach This is the goal state
            if i == len(s1) and j == len(s2):
                return True 
            # using memo
            if (i,j) in dp:
                return dp[(i,j)]

            if i < len(s1) and s1[i] == s3[i+j] and topDownBacktrack(i+1,j) : # Checking if we take the s1 substring 
                dp[(i,j)] = True
                return True
            if j < len(s2) and s2[j] == s3[i+j] and topDownBacktrack(i,j+1) : # Checking if we take the s2 substring
                dp[(i,j)] = True
                return True
            dp[(i,j)] = False
            return False
            

        if len(s1) +len(s2) != len(s3):
            return False

        dp = {} #memo : [(i,j)] = True or False, need to only mark false nodes
        

        
        

        # while i <= len(s1) and j <=len(s2) and i+j len(s3):
            
            
            
        return topDownBacktrack(0,0)
        