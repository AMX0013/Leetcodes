import math

class Solution:


    def longestArithSeqLength(self, nums: List[int]) -> int:

        dp = {}
        dpSeq = {}
        # We use both d and the last ele in seq 
        #  This is because we must ensure that the seq is the same seq
        #  In case of [83,20,17,43,52,78,68,45]
            # Seq 17, 52 , d is 35
            # Seq 43,78 , d is 35
                # This could overlap if dict only had the d as key

        # Finally, index alone better than using the element , captures the same uniqueness
        maxSeqLen = 0
        for right in range(len(nums)):
            for left in range(0,right) :
                d = nums[right] - nums[left]
                # The key is going to be diff and last element in the seq
                
                '''
                get() Parameters:
                    get() method takes maximum of two parameters:

                    key - key to be searched in the dictionary
                    value (optional) - Value to be returned if the key is not found. The default value is None.
                '''

                # seq = dp.get( (d,left) ,[nums[left]])
                # seq.append(nums[right])

                dp[(d,right)] = dp.get( (d,left) ,1)+1
                # dpSeq[(d,right)] = dpSeq.get( (d,left) ,[left]).append(nums[right])

                # print("dpSeq.get( (d,left) ,[left]).append(nums[right]) ==",dpSeq.get( (d,left) , [nums[left]]).append(nums[right]))


                # if len(dpSeq[(d,right)]) > maxSeqLen:
                #     print(  "key : ",d , right , "=" ,dpSeq[(d,right)])
                    

                # maxSeqLen = max(maxSeqLen , len(seq))
            

        return max(dp.values())





