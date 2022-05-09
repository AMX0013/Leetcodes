class Solution:
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        def comboTron2( combo, remains , currPtr, result):
            # base case : if remains == 0:
                #add combo into the result
            if remains == 0:
                result.append(list(combo))  # a copy of it
                return
            
            for nextPtr in range( currPtr,len(candidates)  ):
                #skip duplicates:
                if nextPtr > currPtr and candidates[nextPtr] == candidates[nextPtr-1]:
                    continue
                
                
                pick = candidates[nextPtr]
                
                if remains - pick <0:
                    break # kill func since we have sorted the candidates and no combo exists
                #else we add the pick
                combo.append(pick)
                comboTron2(combo,remains-pick,nextPtr+1,result)
                combo.pop()
            
            
        candidates.sort()
        
        result = []
        combo = []
        
        comboTron2(combo,target,0,result)
        return(result)