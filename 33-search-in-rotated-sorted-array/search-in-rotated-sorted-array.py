class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Initially nums sorted in ascending order

        # The nums was pivoted at an unknown pivot index k (1 <= k < nums.length) 
        #  such that
        # [0,1,2,4,5,6,7]
        # BEcomes : [4,5,6,7,0,1,2].

        # Observation :
            #  from L , it increases to MAx value
            # from R, it decreases to min value

            # So if we have to look for the target:
            # we must understand how to move after landing at mid
            # Eg : [4,5,6,7,0,1,2]


        L = 0
        R = len(nums)-1

        while L<=R:
            
            mid = (L+R) //2
            print("L",L,"R", R, "mid", mid)
            if target  == nums[mid] :
                return mid

            if nums[mid] >= nums[L]:
                # we in the left subset

                # here, only time we move towards the right is if the 
                # target > nums[mid]
                # or when
                # target < nums[L]
                if target > nums[mid] or target < nums[L]:
                    L = mid+1
                else:
                    R =mid - 1
                    
            else: 
                # We in the right half
                # Only time to move left, is when 
                # tgt < nums[mid]
                # or
                #  target > nums[R] 
                if target < nums[mid] or target > nums[R]:
                    R =mid - 1
                else:
                    L = mid+1


        return -1

