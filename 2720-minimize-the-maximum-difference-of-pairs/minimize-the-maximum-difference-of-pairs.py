class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        
        def validMaxdiff(thresh):
            # given this threshold, can we find p pairs ?
            # This func returns true if we find p pairs that are <= thresh
            i = 0
            count_pairs = 0
            while i <len(nums)-1:
                if nums[i+1] - nums[i] <= thresh:
                    count_pairs+= 1
                    # Note pairs cannot have an element reused
                    # hence we increment over the "pair"
                    i+=2
                else:
                    i+=1
                if count_pairs == p:
                    return True
            return False
            
        # Greedy : We sort the input so that we can check 
        # only immediate left or right neighbors
        # this enables to identify pairs
        nums.sort()
        print(nums)
        l = 0                    #The least value a pair's difference can be
        r = nums[-1] - nums[0]   #The max Element in a sorted array, This will yield
        res = r-l                #literal max value of the difference


        # only edge case where they ask for 0 pairs, max(0)
        if p == 0:
            return 0

        while l <=r:
            print(l,r)
            # The kewl way to acc calc mid
            mid = l + (r-l)//2
            print(mid)
            if validMaxdiff(mid):
                res = mid
                # lets try reducing the threshold
                r = mid-1
            else: # looks like this value of a threshold (mid)is too strict, inc
                l = mid+1
        return res 