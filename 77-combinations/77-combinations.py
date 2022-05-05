class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        
        #base case: recursion reaches here first
        if k ==1:
            for i in range(1,n+1):
                result.append([i])  # returns [1,...,n]
            return result
        
        else: # will create +1 digit combinations of returned result
            #print("k level =",k)
            result = self.combine(n,k-1)
            #print(result)
            tempNewRes = []
            x = None
            for y in range(len(result)) :
                atleast = max(result[y])
                #print("#subcombo of Result :",result[y])
                #print("atlest = ", atleast)
                for i in range(atleast+1,n+1):
                    # will create +1 digit combinations of returned result
                    x = result[y][:] # idek how but using [:] sends a copy instead of the whole shit , preventing result[y] from being modified
                    #print("before",x)
                    x.append(i)
                    #print("after",x)
                    tempNewRes.append(x)
                    x = None
                    #print("final subcombo",result[y],result)
            result = tempNewRes
            return result
                