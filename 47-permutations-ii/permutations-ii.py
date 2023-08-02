# class Solution:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:

#         if len(nums)==1:
#             return [nums]
        
#         memo = {}

#         def recur(splice):
#             res = []
            

#             if str(sorted(splice)) in memo:
#                 return memo[str(sorted(splice))]

            
#             if len(splice) == 1:
#                 memo[str(splice)] = [splice[:]]
#                 return [splice[:]]

#             for _ in range(len(splice)):
                
#                 head = splice.pop(0)

#                 perms = recur(splice)
#                 # print(splice,perms)
#                 for perm in perms:
#                     perm.append(head)
#                     if perm not in res:
#                         res.append(perm)
#                 splice.append(head)

#             memo[str(sorted(splice))] = res               

#             return res
#         res = recur(nums)

#         for key , value in memo.items():
#             print(key," : ",value)
        

#         return res



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
            for i in range(len(splice)):
                splice_copy = splice[:]
                head = splice_copy.pop(i)
                perms = recur(splice_copy)
                for perm in perms:
                    perm= [head] + perm
                    if perm not in res:
                        res.append(perm)

            memo[key] = res
            return res
        res = recur(nums)
        for key , value in memo.items():
            print(key," : ",value)
        return res
