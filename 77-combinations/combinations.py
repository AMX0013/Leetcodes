class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        memo = {}
        res = []
        def recur(startIndex,combination):
            if len(combination) == k:
                res.append(combination.copy() )
                return
            for i in range (startIndex, n+1):
                # To current combination, add current element
                combination.append(i)
                # Find all combinations for the new combo
                recur(i+1 ,combination)
                # remove added element to prep for next element combos
                combination.pop()
            return
        recur(1,[])


        return res

