class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        memo = {}
        res = []
        def recurSum(index,combo_arr,total):
            
            if total == target:
                if combo_arr not in res:
                    res.append(combo_arr.copy())
                    return
            if total > target or index >=len(candidates):
                return
            
            # 1st call considering the element too
            combo_arr.append(candidates[index])
            recurSum(index , combo_arr, total+candidates[index])

            # pop from curr, before next one

            combo_arr.pop()

            #2nd call without having the element
            recurSum(index+1 , combo_arr, total)


        recurSum(0,[],0)
        return res
        




