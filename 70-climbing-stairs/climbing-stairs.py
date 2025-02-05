class Solution:
    def climbStairs(self, n: int) -> int:
        # Goal reach top, n steps away
        # u can take 1 or 2 steps at once
        # how many distinct ways can you reach the top
        memo=defaultdict(int)

        # Option 1 : recur with memo [not DP]
        def recur(stage: int):
            if stage > n:
                return 0
            if stage == n:
                return 1
            if stage in memo.keys():
                return memo[stage]

            memo[stage] = recur(stage+1) + recur(stage+2)

            return memo[stage]
        
        return recur(0)