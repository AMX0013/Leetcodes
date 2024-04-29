class Solution {
public:
    void sortColors(vector<int>& nums) {
        int low_ptr = 0;
        int mid_ptr = 0;
        int high_ptr = nums.size()-1;

        while (mid_ptr <= high_ptr){
            if (nums[mid_ptr] == 0){
                int temp = nums[low_ptr];
                nums[low_ptr++] = nums[mid_ptr];
                nums[mid_ptr++] = temp;
            }
            else if (nums[mid_ptr] == 1){
                mid_ptr++;
            }
            else if (nums[mid_ptr] == 2){
                int temp = nums[high_ptr];
                nums[high_ptr--] = nums[mid_ptr];
                nums[mid_ptr] = temp;

            }
        }

    }
};