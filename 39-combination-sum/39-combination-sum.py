class Solution:
    
    def combitron(self, candidates, target, decision, tempRes , result):
        # initially, 
        # if decision == True  i.e we continue to add elements and check
        #print(">>>>    res count :",len(result),result)
        #print("curr combo lenghth",len(tempRes) , tempRes)
        if decision == True:
            # add num from nums:
            for i in range(len(candidates)) :
                num = candidates[i]
                if target-num > 0:
                    tempRes.extend([num])
                    #print(">0 tempres", tempRes)
                    self.combitron(candidates[i:],target-num,decision, tempRes , result)
                    tempRes.pop()
                elif target-num ==0:
                    tempRes.extend([num])
                    if tempRes not in result:
                        result.append(tempRes[:])
                        #print("== tempres", tempRes)
                        #print("== res",result)
                    x = tempRes.pop()
                    
                        
                    return
            
        
            
            
                    
        
        
        #if decision == False:
            # remover the previously added element and go ahead and try the next element
            
        #
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        length = len(candidates)
        result = []
        decision = True
        for i in range(length):
            self.combitron(candidates[i:length],target,decision, [],result)
            
        print(result)
        return result
             
        
                
        