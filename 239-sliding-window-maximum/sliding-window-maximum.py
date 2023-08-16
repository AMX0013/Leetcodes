class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        window=[]

        if k == 1:
            return nums
        if k == len(nums):
            return [max(nums)]

        # use queue to store the indices
        q = collections.deque()


        # TODO: Track the index of the element that is max 

        head = 0
        tail = 0

        

        # Moonwalking worm
        while tail <len(nums):
            
            # print(q)

            # Before we insert a new value into the queue, pop smaller values from right
            while q and nums[q[-1]] < nums[tail]:
                q.pop()
            # The number of pops indicate till where head would have moved
            q.append(tail)

            # q will house indices as is, q[0] always houses the max element

            # pop that max's index if it passes beyond head
            if head > q[0]:
                q.popleft()

            # move head after tail has grown to lenght k
            if tail+1 >=k:
                # add to window list
                window.append(nums[q[0]])
                # drag head
                head+=1

            # move tail
            tail+=1

        
        return window