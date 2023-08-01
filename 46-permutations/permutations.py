class Solution:

      
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        if len(nums) == 1:
            return [nums[:]]
 

        def recur(splice):
            res  = []

            if len(splice) == 1:
                return [splice[:]]
            
            for _ in range(len(splice)):

                # pop the 0th element 
                # eg: in [1,2,3]
                # i0 = 1
                i0 = splice.pop(0)

                # We will finde the perms of this smaller subarray, then append i0
                # to all of them
                
                perms = recur(splice)  #splice = [2,3]

                # perms = [[2,3],[3,2]]
                for perm in perms:
                    perm.append(i0)
                # perms = [[2,3,1],[3,2,1]]


                res.extend(perms)

                # finally to continue permutating, generate the next iteration of the splice
                splice.append(i0)
                # now splice = [2,3,1]
            return res
            


        
        return recur(nums)
            
            
            
        