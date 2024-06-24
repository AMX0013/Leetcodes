class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lenA = len(nums1)
        lenB = len(nums2)

        if lenA > lenB:
            lenA, lenB = lenB, lenA
            nums1, nums2 = nums2, nums1

        total = lenA + lenB
        half = total//2
        # start with the smaller to find the left partition 
        l = 0
        r = lenA -1

        while True:
            A_mid = (l + r)//2
            B_mid = half-1 - A_mid -1
            # if A_mid out of bounds, turn it to infinity based on lrft or right partition
            A_left = nums1[A_mid] if A_mid >=0 else float('-inf')
            A_right = nums1[A_mid+1] if (A_mid + 1) < lenA else float('inf')

            B_left = nums2[B_mid] if B_mid >=0 else float('-inf')
            B_right = nums2[B_mid +1]  if (B_mid + 1) < lenB else float('inf')

            # print (A_left, A_right)
            # print(B_left, B_right)
            
            # shrink A_right if A_left > B_right 
            if A_left > B_right :
                # print(" A_left > B_right ")
                r = A_mid-1
            
            # shrink B_right if B_left > A_right
            elif B_left > A_right :
                # print(" B_left > A_right ")
                l = A_mid + 1
            
            else: # A_left <= B_right and B_left <= A_right
                # if half is even, 
                if total %2 == 0:
                    # median is the ( max(A_left and B_left) + min(A_right, B_right) ) //2
                    return ( max(A_left , B_left) + min(A_right, B_right) ) /2
                # if half is odd
                else:
                    # median is the half'th element
                    # min(rights) or amx ( lefts?)
                    # return max(A_left, B_left)
                    return min(A_right, B_right)
