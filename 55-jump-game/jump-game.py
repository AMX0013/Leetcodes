class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1


        for i in range(goal-1,-1,-1):
            print(i,goal)
            if nums[i] >= goal-i:
                diff = goal-i
                goal = goal - diff
            # max jump
            if i == 0 and nums[i] + i <goal:
                return False
        return True