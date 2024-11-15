class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        if len(quantities) == n:
            return max(quantities)
        quantities.sort()
        
        def binSearch(l,r) -> int:
            
            def validate(x) -> bool:
                # print("Trying minimised MAxVal:", mid)
                storesfilled = 0
                for quantity in quantities:
                    storesfilled += math.ceil(quantity/x)
                # print("stores filled by maxVal:", storesfilled)
                return storesfilled 

            while l<r:
                print(l,r)
                mid = l+ (r-l)//2
                storesFilled = validate(mid)
                if storesFilled > n:
                    # increase to bigger trail
                    l= mid+1
                else:
                    r=mid
            return l
        return binSearch(1, max(quantities))

        