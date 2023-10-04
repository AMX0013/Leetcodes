class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        
        // not the actual LIS
        // implement BS to store the next number in seq
        // the LIS generated is wrong, purely to find length only

        vector<int> res_LIS;
        res_LIS.push_back(nums[0]);             //.push_back > push()
        for(int i=1; i<nums.size(); i++){
            // add to end of res_LIS if greater
            if( nums[i] > res_LIS.back() ){       //.back() > arr[-1]
                res_LIS.push_back(nums[i]);
            }
            else {
                // The lower_bound(first,last,val) function in C++ is a standard library function
                //  that returns an iterator to the first element in the range [first, last) 
                // that is not less than val. 

                // In this case, the range of elements is "res_LIS.begin()" and "res_LIS.end()", 
                // which are iterators pointing to the beginning and end of a vector named "res_LIS".

                // 1. begin() :- This function is used to return the beginning position of the container.
                // 2. end() :- This function is used to return the after end position of the container.
                    
                int mid = lower_bound(res_LIS.begin() , res_LIS.end(),nums[i]) - res_LIS.begin() ;
                res_LIS[mid] = nums[i];
            }
        }

        return res_LIS.size();
    };
};