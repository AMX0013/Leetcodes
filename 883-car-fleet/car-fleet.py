class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # Given the target, calculate time each will take to reach it,
        #  and sort positions in an order repreentable on the scale

        speedTime =[]
        for i in range(len(position)):
            speedTime.append((position[i], (target-position[i])/speed[i]  ))

        speedTime.sort(reverse = True)
        # print(speedTime)
        # fleets = 0
        # We'll use len of stack instead. Pop all those that are going to reach earlier than stack top, append later mfs
        stack = []
        for start, ttr in speedTime:
            if len(stack) >0 and ttr <= stack[-1][1]:
                # this will collide
                continue
            else:
                # new slowpoke, who wont collide
                stack.append((start, ttr))

        return len(stack)
        