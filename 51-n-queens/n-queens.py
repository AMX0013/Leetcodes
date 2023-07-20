class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        if n == 1:
            return [["Q"]]
        if n==2 or n ==3 :
            return res

        
        

        # need a way to store no go zones : the i and j , the positive dignals , the negative diagnals
        horizontal_set = set()         # holds j value
        positive_diag_set = set()      #holds i+j value
        negative_diag_set = set()      #holds i-j value


        dp = [ ["."]*n for _ in range(n)]
        print(dp)

        def placeQueen(i):
        # Top to down

            if i==n:
                # reached out of array, successfully created n queens!
                copyList = ["".join(rows) for rows in dp]
                print(copyList)
                res.append(copyList)
                return

           
            for j in range(n):
                if j not in horizontal_set and \
                i+j not in positive_diag_set and \
                i-j not in negative_diag_set:
                    
                    dp[i][j] = "Q"
                    
                    horizontal_set.add(j)
                    positive_diag_set.add(i + j)
                    negative_diag_set.add(i - j)
                    print(dp)

                    placeQueen(i+1) 


                    # remove placed queen
                    dp[i][j] = "."                   
                    horizontal_set.remove(j)
                    positive_diag_set.remove(i + j)
                    negative_diag_set.remove(i - j)
        placeQueen(0)

        return res


                    
             
            


            