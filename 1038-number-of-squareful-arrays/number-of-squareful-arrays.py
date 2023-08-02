import math
class Solution:
    

    def is_perfect_square(self,num):

        """
        Returns True if num is a perfect square, False otherwise.
        """
        return math.sqrt(num).is_integer()
    def numSquarefulPerms(self, nums: List[int]) -> int:
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
                    print("[",head,"] + ",perm,":",[head] + perm)
                    perm= [head] + perm
                    if perm not in res and self.is_perfect_square(perm[0]+perm[1]) :
                        res.append(perm)
                splice.append(head)
            memo[key] = res
            return res
        res = recur(nums)
        print(res)


        for key , value in memo.items():
            print(key," : ",value)

        return len(res)