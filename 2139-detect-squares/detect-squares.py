class DetectSquares:

    def __init__(self):
        self.grid = {}
        

    def add(self, point: List[int]) -> None:
        self.grid[(point[0], point[1])] = self.grid.get( (point[0], point[1]), 0 ) + 1
        #  Duplicate points are allowed and should be treated as different points.
        return

    def count(self, p: List[int]) -> int:
        count = 0
        for d in self.grid.keys():
            # find one p is valid, use that and check if dictionary has other 2
            # since square, donal is critical
            
            if abs(d[0] - p[0]) == abs(d[1] - p[1]) and abs(d[1] - p[1]) >0 :
                dxpy    = (d[0], p[1])
                pxdy    = (p[0], d[1])
                point   = (p[0], p[1])
                diag    = (d[0], d[1])
                
                if dxpy in self.grid and pxdy in self.grid:
                    num_sqrs = self.grid.get(diag)  * self.grid.get(dxpy) * self.grid.get(pxdy)

                    # print(num_sqrs)
                    # if point in self.grid:
                    #     num_sqrs*=self.grid.get(point)
                        # print(num_sqrs)
                    # print('dxpy',dxpy,self.grid.get(dxpy))
                    # print('pxdy',pxdy,self.grid.get(pxdy))
                    # print('point',point,self.grid.get(point))
                    # print('diag',diag,self.grid.get(diag))
                    count+=num_sqrs
        
        # print('Ans: ',count)
        # print()
        return count


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)