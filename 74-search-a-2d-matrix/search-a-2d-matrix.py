class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        i_left = 0
        # vertical ptr i
        i_right = len(matrix)-1
        


        j_left = 0
        # vertical ptr j
        j_right =len(matrix[0])-1
        

        while i_left<= i_right :
            mid_i = (i_left+i_right)//2
            print("--i--",mid_i)

            # mid_i indicates the row in question
            # [x,.....,y]
            if target > matrix[mid_i][-1] : #target > y
                i_left = mid_i+1
                
            elif target < matrix[mid_i][0]:  #target < x
                i_right= mid_i-1

            else:  #element in current row
           

                # Now find row using binary search
                while j_left <= j_right:

                    mid_j = (j_left+j_right)//2
                    print("----j----",mid_j)

                    if matrix[mid_i][mid_j] == target:
                    # found the column
                        return True

                    

                    elif matrix[mid_i][mid_j] < target:
                        j_left = mid_j+1
                    else: 
                        j_right = mid_j-1
                
                return False

        return False