class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        N = len(height)
        mono_stack = []
        for idx in range(N):           
            # print("for idx = ",idx, mono_stack)
            while len(mono_stack) > 0 and height[mono_stack[-1]] < height[idx]:
                # keep comparing till the gaps are filled
                pop_id = mono_stack.pop() #the cavity to be filled
                # find next stack top
                if len(mono_stack) == 0:
                    break

                gap = idx - mono_stack[-1]  - 1
                
                min_tower = min(height[idx], height[mono_stack[-1]] ) - height[pop_id] #pop_id indicates the floor
                # print(gap, min_tower)
                res +=( gap * min_tower)

            mono_stack.append(idx)

        return res


            
                
        