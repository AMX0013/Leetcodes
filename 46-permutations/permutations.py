class Solution:

      
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # backtracking, as in find permutations of the smaller set
        def recur( nums: List[List[int]]):
            

            if len(nums) == 1:
                return [nums[:]]
            res = []
            for i in range(len(nums)):
                # reduce
                popped = nums.pop(0)
                # obtain permutations of smaller set
                perms = recur(nums)
                # put it back, but diff loc right? like a queue?
                nums.append(popped)

                # create your permutations
                for perm in perms:
                    perm.append(popped)

                res.extend(perms)
            return res

        res = recur(nums)

        return res
        
            
            
            
        