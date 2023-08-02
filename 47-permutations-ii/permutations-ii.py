class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        if len(nums)==1:
            return [nums]
        
        def recur(splice):
            res = []

            if len(splice) == 1:
                return [splice[:]]

            for _ in range(len(splice)):

                head = splice.pop(0)

                perms = recur(splice)
                print(splice,perms)
                for perm in perms:
                    perm.append(head)
                    if perm not in res:
                        res.append(perm)

                splice.append(head)

            return res

        # recur(nums)

        return recur(nums)