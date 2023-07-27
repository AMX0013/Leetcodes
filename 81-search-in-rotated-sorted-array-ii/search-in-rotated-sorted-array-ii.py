class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        L = 0
        R = len(nums)-1

        def recurBinSearch(L,R):
            while L<=R:

                mid = (L+R) //2
                print("L",L,"R", R, "mid", mid)
                if target  == nums[mid] :
                    return True

                if nums[mid] > nums[L]:
                    # we in the left subset

                    # here, only time we move towards the right is if the 
                    # target > nums[mid]
                    # or when
                    # target < nums[L]
                    if target > nums[mid] or target < nums[L]:
                        L = mid+1
                    else:
                        R =mid - 1

                elif nums[mid] < nums[L] : 
                    # We in the right half
                    # Only time to move left, is when 
                    # tgt < nums[mid]
                    # or
                    #  target > nums[R] 
                    if target < nums[mid] or target > nums[R]:
                        R =mid - 1
                    else:
                        L = mid+1
                else:
                    return recurBinSearch(L,mid-1) or recurBinSearch(mid+1,R)
        
        return recurBinSearch(L,R)