class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)**2
        a=1
        d=1
        sumFormula = int((n/2)*(2*a + (n-1)*d))
        total = 0
        map = [0]*n
        # print(map)
        res = []
        for arrs in grid:
            total += sum(arrs)
            for num in arrs:
                map[num-1]+=1
                if map[num-1]==2:
                    res.append(num)
        actual= total -res[0]
        missing = sumFormula - actual
        res.append(missing)

        return res
        
        