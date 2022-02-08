class Solution:
    
    def inInterval(self,curr,next):
        
        if next[0] <= curr[1] and next[1] > curr[1]:
            res = [curr[0] , next[1]]
            return res
        elif next[0] <= curr[1] and next[1] <= curr[1]:
            res = [curr[0] , curr[1]]
            return res
        else:
            return None
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        outputList = []
        i=0
        base = []
        base.append(intervals[i][0])            
        base.append(intervals[i][1])
        i+=1
        if i ==  len(intervals):
                    outputList.append(base)
        while i < len(intervals):    
            
            itr = []
            itr.append(intervals[i][0] )           
            itr.append(intervals[i][1] )
            res = self.inInterval(base,itr)
            if res :
                base.pop()
                base.append(res[1])
                print(i,base)
                i+=1
                if i ==  len(intervals):
                    outputList.append(base)
            else:
                outputList.append(base)
                print(i,">popped base:",base)
                base = itr
                print(i,">new base:",base)
                i+=1
                if i ==  len(intervals):
                    outputList.append(base)
        return outputList
                
                
            
            
            
            
            
            
            
            
            
           