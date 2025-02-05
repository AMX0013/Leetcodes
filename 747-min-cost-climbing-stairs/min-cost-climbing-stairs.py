class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        costMemo = defaultdict(int) 
        def recur(step: int):
            # caching
            if step in costMemo.keys():
                return costMemo[step]
            # stopp condition1 : notice how its len(cost),
            #  the index that 1 larger that the last visitable index in a zero indexed array
            if step == len(cost) :
                return 0
            # stopp condition2
            if step > len(cost):
                return 10**9
            # init
            if step == -1:
                costMemo[step] = min(recur(step+1), recur(step+2))
            else:
                costMemo[step] = cost[step]+ min(recur(step+1), recur(step+2))

            return costMemo[step]
            
        # call 
        recur(-1)
        return min(costMemo[0], costMemo[1])