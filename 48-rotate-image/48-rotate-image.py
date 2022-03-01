class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        lenth = len(matrix)-1
        
        top = 0
        left = 0
        leftmost=0
        bottom = lenth
        right = lenth
        
        print("top : ",top, "left: ", left , "bottom : ",bottom, "right : ", right )
        for i in range(len(matrix)):
            print(matrix[i])
        print("______init_____")
        
        while bottom > top:
            while right > left:
                    
                    print("top : ",top, "left: ", left , "bottom : ",bottom, "right : ", right )
                    temp = matrix[top][left]
                    matrix[top][left] = matrix[lenth-left][top]
                    matrix[lenth-left][top] = matrix[lenth-top][lenth-left]
                    matrix[lenth-top][lenth-left] = matrix[left][lenth-top]
                    matrix[left][lenth-top] = temp
                    
                    
                    left = left+1
                    
                    for i in range(len(matrix)):
                        print(matrix[i])
                    print("top : ",top, "left: ", left , "bottom : ",bottom, "right : ", right )
                    print("___________")
                    
            leftmost = leftmost+1
            left = leftmost
            right = right-1
            top = top+1
            bottom = bottom-1

'''

                    matrix[top][left] = matrix[right-left][top]
                    matrix[right-left][top] = matrix[bottom-top][right-left]
                    matrix[bottom-top][right-left] = matrix[left][bottom-top]
                    matrix[left][bottom-top] = temp


'''
        
            