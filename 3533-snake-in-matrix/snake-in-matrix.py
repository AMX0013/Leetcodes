class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        
        grid = [[None for _ in range(n)]for _ in range(n)]
        # print(grid)
        src = (0,0)
        for cmd in commands:
            match cmd:
                case "DOWN":
                    src = ( min(src[0]+1 , n-1),src[1])
                case "UP":
                    src = (max(src[0]-1 , 0),src[1])
                case "LEFT":
                    src = (src[0],max(src[1]-1 , 0)) 
                case "RIGHT":
                    src = (src[0],min(src[1]+1 , n-1)) 
            print(src)

        return src[0]*n + src[1]
                
