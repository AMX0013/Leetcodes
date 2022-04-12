class Solution:
    def __innit__():
        self.resStr = ""
        self.resCount = 0
    def decToBin(self , num,StringMemo,CountMemo):
        
        if num >= 1:
            if StringMemo[num]!= None and CountMemo[num] != None:
                self.resStr += StringMemo[num]
                self.resCount += CountMemo[num]
                num = 0
            else:
                self.decToBin(num//2,StringMemo,CountMemo )
        self.resStr += str(num%2)

        self.resCount += int(num%2)
    #print(num,"resCount",resCount,">",resStr)
        StringMemo[num] = self.resStr        
        CountMemo[num] = self.resCount                    
        
        
        
    def countBits(self, n: int) -> List[int]:
        StringMemo = {x:None for x in range(n+1) }
        CountMemo = {x:None for x in range(n+1) }
        result = []
        for i in range(n+1):
            self.resStr = ""
            self.resCount = 0
            self.decToBin(i,StringMemo,CountMemo)
            
            #print("count of 1s>",CountMemo[i],"str>>",StringMemo[i],"no, >",i)
            result.append(CountMemo[i])
                            
        print("________")
        print(StringMemo)
        print("________")
        print(CountMemo)
        print("____________________")
                            
        return result
        
            
"""
        if StringMemo[num]!= None and CountMemo[num] != None:
            self.resStr += str(num%2)
            self.resCount += int(num%2)
        else:
"""

                
            
    
            
            
            
        
        