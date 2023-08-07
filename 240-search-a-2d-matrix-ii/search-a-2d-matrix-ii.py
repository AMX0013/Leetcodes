class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        #          C
        #       +----+----+----+----+----+
        #       |  1 |  4 |  5 | 11 | 15 |
        #       +----+----+----+----+----+
        #       |  2 |  5 |  8 | 12 | 19 |
        #       +----+----+----+----+----+
        #       |  3 |  6 |  9 | 16 | 22 |
        #       +----+----+----+----+----+
        #       | 10 | 13 | 14 | 17 | 24 |
        #       +----+----+----+----+----+
        #    r> | 18 | 21 | 23 | 26 | 30 |
        #       +----+----+----+----+----+


        r = len(matrix)-1
        c = 0
        height,width = len(matrix)-1 , len(matrix[0])
        print(r,c,matrix[r][c])
        while r>=0 and c< width:
            print(r,c,matrix[r][c])


            # look inward (left side)
            if target ==  matrix[r][c]:
                return True
                
                
            # look outward (right side)
            elif target > matrix[r][c] :
                print("target > matrix[r][c]")
                c+=1
            else:
                # target < matrix[r][c]:
                print("else")
                r-=1 

        return False           
