class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        combo = []
        def recur(combo: List[int], i: int, cum_sum: int):
            if cum_sum == target:
                res.append(combo[:])
                return 
            if i>=len(candidates) or cum_sum >= target:
                return
            # if including num[i], then i wont inc
            combo.append(candidates[i])
            recur(combo, i, cum_sum + candidates[i])
            # remove the element added
            combo.pop()
            # not including anymore instances of num[i]
            recur(combo, i+1, cum_sum)

        recur(combo, 0, 0)         
                    
        return res
        




