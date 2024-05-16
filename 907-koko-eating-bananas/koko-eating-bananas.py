class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # goal: return the min speed to consume bananas
            # max speed would be max(piles) per hour
        # necessary speed = sum(piles)/total time

        def binary_search( arr ):

            def condition(mid):
                # print("at speed: ", mid)
                time =0
                for pile in piles:
                    time += ceil(pile/mid) 
                # print("time taken = ", time)
                if time <= h:
                    # 
                    return True    

            # left, right = max(ceil(sum(piles)//h) , 1), max(arr)
            left, right = ceil(sum(piles)/h) , max(arr)

            # print(left, right)
            while left < right:
                
                mid = left + (right-left)//2
                # print("at speed: ", mid)
                if condition(mid):
                    right = mid
                else:
                    left = mid+1
            return left
        
        return binary_search(piles)