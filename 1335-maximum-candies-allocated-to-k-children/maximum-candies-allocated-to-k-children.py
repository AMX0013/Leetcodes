class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        TotalCandies = sum(candies)

        if k > TotalCandies:
            return 0
        l = 1
        r = max(candies)
        sack = 1

        while l<=r:


            candyPerPile = (l+r) // 2
            piles = 0
            for i in candies:
                piles += i//candyPerPile

            # As candyPerPile reduces, no of piles increases
            # aim to maximise candyPerPile
            # bring pile size to k, or as close as to k
            print("candyPerPile, ",candyPerPile ,"piles",piles , "k",k)

            if piles >= k:
                l = candyPerPile+1
                sack  = max(sack,candyPerPile)
            
            else:              
                
                r = candyPerPile-1

                
        return sack