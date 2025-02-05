class Solution:
    def climbStairs(self, n: int) -> int:
        # bottom up: from the dest to src
        # check moves from n-1
        # given: no of moves
        moves = 2
        # maintain a deque of fixed len, pop, and append left
        # below is n-th place and nth place values, indicating in how many moves can they reach
        # [1][1]
        # In 1 step from n-1
        ways = deque()
        # init
        ways.append(1)
        ways.append(1)
        # print(ways)
        for i in range(n-1):        # n-1 cuz we computed one step, from the n-1th place 
            newNumOfWays = sum(ways)
            ways.pop()
            ways.appendleft(newNumOfWays)
            # print(ways)
        return ways[0]