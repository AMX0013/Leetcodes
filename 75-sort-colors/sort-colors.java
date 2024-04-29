class Solution {
    public void sortColors(int[] nums) {
        
        int low_ptr = 0;
        int mid_ptr = 0;
        int high_ptr = nums.length - 1;

        while (mid_ptr<=high_ptr){
            if (nums[mid_ptr] == 0){
                // swap with low_ptr
                //System.out.println("swapping mid nums["+mid_ptr+"] "+nums[mid_ptr]+" with low nums["+low_ptr+"] : "+ nums[low_ptr]);
                int temp = nums[low_ptr];
                nums[low_ptr] = nums[mid_ptr];
                nums[mid_ptr] = temp;
                low_ptr+=1;
                mid_ptr+=1;
            }
            else if (nums[mid_ptr] == 1){
                //System.out.println("mid nums[mid =1]");
                mid_ptr+=1;
            }
            else if (nums[mid_ptr]== 2){
                // swap with high_ptr
                 //System.out.println("swapping mid nums["+mid_ptr+"]: "+nums[mid_ptr]+" with high nums["+high_ptr+"] : "+ nums[high_ptr]);
                int temp = nums[high_ptr];
                nums[high_ptr] = nums[mid_ptr];
                nums[mid_ptr] = temp;
                high_ptr-= 1;
                // mid_ptr+=1;
            }
            //System.out.println(Arrays.toString(nums));
            
        }
    }
}