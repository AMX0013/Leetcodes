class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # put numbers post sorting into groups, based on the limit
        groups = []
        num_group_map = defaultdict(int)

        for num in sorted(nums):
            # if the groups is empty, or the diff betwwen the curr and prev greater than limit
            if not groups or num - groups[-1][-1] > limit:
                # add a new list X , use deque, as popleft will recreate indices of list, makin it O(n)
                groups.append(deque())
            # add to the latest group in groups, the num
            groups[-1].append(num)
            num_group_map[num] = len(groups)-1
        
        for idx,num in enumerate(nums):
            grpId = num_group_map[num]
            nums[idx] = groups[grpId].popleft()

        return nums

        