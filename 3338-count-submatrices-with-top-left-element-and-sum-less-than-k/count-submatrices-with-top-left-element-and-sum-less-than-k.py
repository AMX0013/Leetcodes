class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        if k < grid[0][0]:
            return 0
        
        src = grid[0][0]
        
        
        def prefixsum(arr):
            # vertical prefixsum
            for j in range(len(grid[0])):
                for i in range(1,len(grid)):
                    arr[i][j] += arr[i - 1][j]
             
            # horizontal prefixsum
            for i in  range(len(grid)):
                for j in range(1, len(grid[0])):
                    arr[i][j] += arr[i][j - 1]
        
        num = 0
        prefixsum(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] <= k:
                    num +=1
        return num
            
                
        