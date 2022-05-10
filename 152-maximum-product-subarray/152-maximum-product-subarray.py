class Solution:
    
    #bruteforce
    # works best when there are very few -ve or 0
    '''
    def recursive(self,inputNums, subSeq ,result,currProd,maxim):
        subMax = maxim
        for i in range(len(inputNums)):
            if inputNums[i] <= 0 :
                # dict(currProd) = subSeq so far
                result[currProd].append(list(subSeq))
                subMax = self.recursive(inputNums[i+1:],[],result,1,maxim)
                
            
            
            currProd *=  inputNums[i]
            if currProd > maxim:
                maxim = currProd
                #print(maxim)
            subSeq.append(inputNums[i])
            result[currProd].append(list(subSeq))
            if subMax > maxim:
                maxim = subMax
        return maxim
     '''       
                
            
        
    
    
    def maxProduct(self, nums: List[int]) -> int:
        localMax =1
        localMin =1
        '''
        maxim = -math.inf
        result = defaultdict(list)
        output = self.recursive(nums,[],result,1,maxim)
        '''
        
        res = max(nums)
        for num in nums:
            if num == 0:
                localMax =1
                localMin =1                
                continue
            tempMax = num*localMax
            localMax = max(num, num*localMax , num*localMin )
            localMin = min(num, tempMax      , num*localMin )
            res = max(localMax,res)         
        
        #print(result[output],result,output )
        return res
            
            
        