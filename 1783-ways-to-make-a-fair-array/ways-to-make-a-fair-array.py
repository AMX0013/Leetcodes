class Solution:

    # Template for prefix sum
    # prefixSum = []
    # prefixSum.append(init_ele)
    # for :
        # prefixSum.append( prefixSum[-2] + nums[i] )
    
    def waysToMakeFair(self, nums: List[int]) -> int:
        #Larry's template for prefix sum

        prefixSum = list()
        suffixSum = list()

        def computePrefixSum(nums, prefix, copyUntil):
            for index, num in enumerate(nums):
                if index <copyUntil:
                    prefix.append(num)
                    continue
                prefix.append( prefix[-2] + num )

        computePrefixSum(nums, prefixSum, 2)
        computePrefixSum(nums[::-1], suffixSum, 2)
        suffixSum.reverse()
        # print(prefixSum)
        # print(suffixSum)

        num_of_ways = 0
        N = len(nums)
        # find the index to be swapped
        for i in range(N):
            # print(">",i, nums[i])
            # before
            oddSum = 0
            evenSum = 0
            if i -1 >= 0:
                oddSum = prefixSum[i-1] 
            if i -2 >= 0:
                evenSum = prefixSum[i-2]
            # print("INIT oddSum :",oddSum,"evenSum: ", evenSum)
            # After            
            if i+2 < N:
                oddSum += suffixSum[i+2]
            if i+1 < N:
                evenSum += suffixSum[i+1]
            # print("FINL oddSum :",oddSum,"evenSum: ", evenSum)
            if evenSum == oddSum:
                # print("works when we remove",i,"'th ele ", nums)
                num_of_ways += 1


        return num_of_ways