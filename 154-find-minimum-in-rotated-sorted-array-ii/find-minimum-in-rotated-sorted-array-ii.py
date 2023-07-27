class Solution:
    def findMin(self, nums: List[int]) -> int:
            
        L = 0
        R = len(nums)-1
        minY = math.inf
        # mid = (L+R)//2

        def pivotFind(L,R,minY):
            while L<= R:
                mid = (L+R)//2
                minY = min(minY,nums[mid])
                print(L,R,mid)
                # [1,2,2,2,0,1,1]
                
                if nums[L] == nums[R]:
                    minY = min(minY,pivotFind(L,mid-1,minY),pivotFind(mid+1,R,minY))
                    return minY

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
                else :
                    # nums[mid] < nums[L]
                    # In right arr
                    R = mid-1
                
            return minY

        minVal = pivotFind(L,R,minY)
        print(minVal)
        return minVal
