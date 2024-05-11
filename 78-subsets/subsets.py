class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        # res.add()
        
        stack = []
        for num in nums:
            stack.append(set([num]))

        # print("stack after population: ",stack)
        while stack:
            subset = stack.pop()
            if sorted(list(subset)) in res:
                continue
            res.append(sorted(list(subset)))

            # print("popped: ",subset)
            # print("stack before: ", stack)
            for num in nums:
                if num in subset:
                    continue
                subset.add(num)
                stack.append(subset.copy())
                subset.remove(num)
            # print("stack now: ", stack)
            # print(res)



        res.append([])

        return sorted(res)


