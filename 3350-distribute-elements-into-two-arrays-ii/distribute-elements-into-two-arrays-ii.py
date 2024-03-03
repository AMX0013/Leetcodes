import bisect

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1=list()
        arr2=list()
        res_arr1=list()
        res_arr2 = list()
        
        arr1.append(nums[0])    #1
        arr2.append(nums[1])    #2
        res_arr1.append(nums[0]) 
        res_arr2.append(nums[1])
        
        for ops in range(3,len(nums)+1):
            idx = ops-1
            num = nums[idx]
            l1 = len(arr1)
            l2 = len(arr2)
            # print("at ",ops, "nums[",idx,"] = ",num)
            # print(l1 ,"-" , bisect.bisect_right(arr1,num), " = ",l1 - bisect.bisect_right(arr1,num) )
            # print(l2 ,"-" , bisect.bisect_right(arr2,num), " = ",l2 - bisect.bisect_right(arr2,num) )

            grCnt_arr1_num = l1 - bisect.bisect_right(arr1,num)
            grCnt_arr2_num = l2 - bisect.bisect_right(arr2,num)
            
            # print("greaterCount(arr1,nums[idx])=",grCnt_arr1_num, "greaterCount(arr2,nums[idx]) =", grCnt_arr2_num  ) 
            
            
            if( grCnt_arr1_num ) > ( grCnt_arr2_num ) or ( ( grCnt_arr1_num ) == ( grCnt_arr2_num ) and l1 <= l2 ):
                bisect.insort_right(arr1,num) 
                res_arr1.append(nums[idx])
            else:  
                bisect.insort_right(arr2,num) 
                res_arr2.append(nums[idx])
        
            # print("arr1 = ",arr1)
            # print("arr2 = ",arr2)
            # print("-----------------------------------")
            
        
        res_arr1.extend(res_arr2)
        
        return res_arr1