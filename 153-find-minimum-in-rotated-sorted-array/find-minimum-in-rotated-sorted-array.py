import math
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Unique elements, ez
        L = 0
        R = len(nums)-1
        minY = math.inf
        # mid = (L+R)//2
        while L<= R:

            

            mid = (L+R)//2
            minY = min(minY,nums[mid])
            print(L,R,mid)

            if nums[mid] >= nums[L]:
                # In left arr
                # the least element must be in the right orrrrr
                # The pivot is L itself

                if nums[L] > nums[R]:
                    # This means right arr is smaller
                    L= mid+1
                else:
                    # This is the sorted arr
                    R = mid-1
            else:
                # In right arr
                R = mid-1

        return minY
