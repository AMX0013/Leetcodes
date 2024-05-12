class Solution:
    # issues
        # no proper memoization, 
        # relies on sorting heavily
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        # res.add()
        
        subset = []
        def dfs(i, subset):
            if i > len(nums)-1:
                res.append(subset[:])
                return
            # add teh element to subset
            subset.append(nums[i])
            dfs(i+1,subset)

            subset.pop()
            dfs(i+1,subset)

        dfs(0,subset)

        return res


