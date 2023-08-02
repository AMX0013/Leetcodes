
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        if len(nums)==1:
            return [nums]
        
        memo = {}

        def recur(splice: List[int]):
            if len(splice) == 1:
                return [splice[:]]

            key = tuple(sorted(splice))
            if key in memo:
                return memo[key]

            res = []
            for _ in range(len(splice)):
                
                head = splice.pop(0)
                perms = recur(splice)
                for perm in perms:
                    perm= [head] + perm
                    if perm not in res:
                        res.append(perm)
                splice.append(head)
            memo[key] = res
            return res
        res = recur(nums)
        for key , value in memo.items():
            print(key," : ",value)
        return res
