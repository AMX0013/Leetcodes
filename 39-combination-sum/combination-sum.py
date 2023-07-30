class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        memo = {}
        res = []
        def recurSum(index,splice,total):
            
            if total == target:
                if splice not in res:
                    res.append(splice.copy())
            if total > target or index >=len(candidates):
                return
            
            # 1st call considering the element too
            splice.append(candidates[index])
            recurSum(index , splice, total+candidates[index])

            # pop from curr, before next one

            splice.pop()

            #2nd call without having the element
            recurSum(index+1 , splice, total)


        recurSum(0,[],0)
        return res
        




