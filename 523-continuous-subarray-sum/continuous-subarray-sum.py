class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        pre_sum = [0 for _ in range(N)]
        pre_sum[0] = nums[0]
        # modulo is CIRCULAR
        # you will hit the same remainder again after adding the denominator only
        # if x%k =z, then (x+k) % k = z

        remainders_map = defaultdict()
        # ghastly init. Done so that, 
        # It works properly for case when 0 is remainder
            # and it is valid. for eg [23,2,4,6,6], k= 7
            # remainder = 0 when i is 3. 
            # if this init didn't exist, it wouldve been the sole instance of the remainder
            # reason its -1 because 
                # if i = 0, that ir k exists as first element, it should not take that.
                # if i = 1, it should take that, as 1-0 would fail, but 1 - (-1) will be 2 
        remainders_map[0] = -1
        
        remainder = 0
        for i in range(N):
            remainder += nums[i]
            remainder %= k

            if remainder not in remainders_map:
                remainders_map[remainder] = i

            elif i - remainders_map[remainder] >=2:
                print(True, remainders_map)
                return True           
        print(False, remainders_map)
        return False
        

        