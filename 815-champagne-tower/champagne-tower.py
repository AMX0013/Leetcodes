class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # We want to simulate the pour
        # Instead of storing it all, we store only 2 layers
        # Assume each cup is of vol 1unit but we transalte poured to extra_drip
        # extra_drip = poured-1
        # use extra_drip to feed its left and right children
        # this alows us to track how much extra each cup contains

        prev_row = [poured]
        


        row_idx = 0

        while row_idx < query_row:
            row_idx +=1
            curr_row = [0 for _ in range(len(prev_row)+1)]
            for i in range(row_idx):
                extra_drip = prev_row[i] - 1
                if extra_drip >0: #it overflows equally to left and right cups below
                    curr_row[i] += 0.5*extra_drip
                    curr_row[i+1] += 0.5*extra_drip
            
            prev_row = curr_row
            print(prev_row)

        print(prev_row)

        return min(1,prev_row[query_glass])