class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        # Pre check if already sorted O(n)
        if (all(nums[i] <= nums[i+1] for i in range(len(nums)-1))):
            return True

        def equalOnesSet(a: int, b: int) ->bool:
            return bin(a).count('1') == bin(b).count('1')

        def swap(x: int, y: int):
            if equalOnesSet(nums[x],nums[y]):
                nums[x], nums[y] = nums[y], nums[x] 
                return True
            else:
                return False

        clone = nums[:]
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if nums[j] > nums[j+1]:
                    if swap(j,j+1):
                        clone[j], clone[j+1] = clone[j+1], clone[j]
                    else:
                        return False

        return clone == nums
        