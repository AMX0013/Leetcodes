class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # ASsumption 1: Rows are sorted
        # Assumption 2: First element of each row is larger than the last element of prev row

        # Can be aligned to gether to form a singular long sorted element

        # First, find the row
        # then search the row

        cols_arr = [matrix[y][0] for y in range(len(matrix))]
        # print(cols_arr)
        col_len = len(cols_arr)

        def Check(mid, arr) -> bool:
            # print("col check", arr[mid])
            if arr[mid] > target:
                return True

        def binary_first(arr, condition):
            # print("BS ing on: ", arr)
            left, right = 0, len(arr)
            while left < right:
                mid = left + (right-left)//2

                if condition(mid, arr):
                    right = mid
                else:
                    left = mid+1
            #  this is the leftmost index where the element would be inserted
            # for the search, return left-1
            return left-1

        condition = Check
        column = binary_first(cols_arr, condition)
        

        row_arr = matrix[column]
        # print(row_arr)

        lindex = binary_first(row_arr, condition)
        # print(lindex,row_arr)

        return (row_arr[lindex] == target)

        



        

        
