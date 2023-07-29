class Solution:
    def soupServings(self, n: int) -> float:
        
        values = {}


        def computeProbability(a,b):

            # Here the idea is to backtrack our way up to the top of the recursion tree
            # The tree is made up of 4 moves, everytime
            # Possibility of choosing a move is 0.25

            # Any node at the subtree will indicate value of the requested probaility for that a,b value
            # To memoize these values, we use a 2D list object or a dict
            if (a,b) in values:
                return values[a,b]

            # We want to return half of the probability that both a and b are empty
            if a<=0 and b<=0:
                return 0.5
            # And Whole of the probability that a is empty only
            elif a<=0 :
                return 1
            elif b<=0:
                return 0
            
            # If thats not the case, we choose 1 of the four options
            # The 0.35 indicates the probability of choosing that option
            values[a,b] = 0.25*(computeProbability(a-100 , b-0)+computeProbability(a-75 , b-25)+computeProbability(a-50 , b-50)+computeProbability(a-25 , b-75))
            return values[a,b]

        if n >= 5000:
            return 1
        return computeProbability(n , n)