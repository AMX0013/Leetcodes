class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums)-k
        l = 0
        r = len(nums) - 1

        def quikSelk(l,r):
            # Quick Select algo:
            # Here we choose a pivot elemnet, in my case its nums[r]
            # Idea is to move a new ptr called fwd only if everly element at i is less than pivot. 
            # So we swap element at i with element at p
            # By this we get a continuous order of ints that are less than the pivot
            # After that, we will end up with fwd at a certail position.
            # This is the rightful position of the pivot element.
                # if our K is before fwd, call recursively from L to fwd-1
                # else fwd+1 to r 

            pivot = nums[r] #We choose this as pivot, can choose other elements too ?
            fwd = l

            for i in range(l,r):
                

                if nums[i] <= pivot:
                   # check if other elements are completely grater, continuously
                    # This is accomplished by moving the pivot along the way
                    # swap i and L's value
                    nums[i] , nums[fwd] = nums[fwd] , nums[i]
                    fwd+=1
            # This is the rightful position of the pivot element.
            # if our K is before fwd, call recursively from L to fwd-1
            # else fwd+1 to r

            nums[fwd] , nums[r] = pivot , nums[fwd]

            if k == fwd:
                return nums[fwd]
                
            else:
                if k < fwd:
                    return quikSelk(l,fwd-1)
                else:
                    return quikSelk(fwd+1,r)
        
        return quikSelk(l,r)



