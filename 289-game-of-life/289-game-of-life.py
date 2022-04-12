class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        
        """
        prevstate = [[None for i in range(len(board[0]))] for j in range(len(board))]
        runs = 0
        for y in range(len(board) ):
            for x in range(len(board[0])):
                prevstate[y][x] = board[y][x]
        x = len(board[0])
        
        y = len(board)
        
        print(x,y)
        while  runs <1:
            runs+=1
            
            print(board)
            for i in range(y):
                for j in range(x):
                    neighbors = 0
                    row = i
                    col = j
                    for direction in range(0,9):
                        if(direction == 4):
                            continue
                        n_row = row + ( (direction%3) -1 )
                        n_col = col + ((direction//3) - 1)
                        if n_row >= 0 and n_row < y and n_col >= 0 and n_col < x:
                            print("neighbor node>",n_row,n_col,prevstate[n_row][n_col])
                            neighbors += prevstate[n_row][n_col]
                            
                            
                    print(">>>i,j =",i,j,"neighbors>",neighbors)
                    
                    if board[i][j] == 1 :#live
                        
                        #1> live cell with fewer than two live neighbors -> dies
                        if neighbors <2:
                            board[i][j] = 0
                        #2>  live cell with two or three live neighbors -> lives on
                        elif neighbors==2 or neighbors ==3:
                            board[i][j] = board[i][j]
                        #3>  live cell with more than three live neighbors -> dies
                        elif neighbors>3:
                            board[i][j] = 0
                    else:
                        #1>  dead cell with exactly three live neighbors becomes a live cell
                        if neighbors == 3:
                            board[i][j] = 1
                    print(">>>i,j =",i,j,"board>",board[i][j])
                    print(">>>i,j =",i,j,"prevstate>",prevstate[i][j])
            print(board)
            print("---------------------------------------------------",runs)
                        
            
        