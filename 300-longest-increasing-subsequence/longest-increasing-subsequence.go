func lengthOfLIS(nums []int) int {
    
    resLIS := make([]int,0)  //int list with len 0

    resLIS = append(resLIS,nums[0])

    for i:=1; i<len(nums); i++ {

        if nums[i] > resLIS[ len(resLIS)-1 ] {
            resLIS = append(resLIS , nums[i])
        }else{

            // The second argument is a function that takes an integer index and returns a boolean value.
            // This function is used to determine whether the search should continue or stop.
            
            // In this case, the function checks whether the value at the current index of resLIS >= nums[i].
            
            // The result of the sort.Search function is assigned to a variable called mid.
            // mid represents the index where nums[i] should be inserted into resLIS to maintain its sorted order.
            // If nums[i] is already present in resLIS, then mid will be the index of its first occurrence.

            mid := sort.Search(len(resLIS) , func(index int) bool { return resLIS[index] >= nums[i] })
            resLIS[mid] = nums[i]
        }
    }

    return len(resLIS)
}