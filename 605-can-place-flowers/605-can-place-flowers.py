class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        sol = n
        n=0
        size = len(flowerbed)
        #print(size)
        #rules
        #1 no adjacent >> if you plant, i+= 2
        #if already planted i+=2
        #if 0, check i-1 & i+1 only if i != 0 or last
        i=0
        
        if size == 1:
            if sol ==1:
                if flowerbed[0] == 0:
                    return True
                else:
                    return False
                    
            elif sol ==0:
                if flowerbed[0] == 1 or flowerbed[0] == 0:
                    return True
                else:
                    return False
            
        
        while i < size:
            if flowerbed[i] ==1:
                i+=1
                #print("1)",i,n, ">",flowerbed)
            elif flowerbed[i] ==0:
                #first element
                if  (i==0 or i ==size-1 ):
                    
                    if  i==0 and flowerbed[i+1]==0 :

                            n+=1
                            flowerbed[i] =1
                            i+=1
                            #print("2)",i,n, ">",flowerbed)

                    #end/last element
                    elif i==size-1 and flowerbed[i-1]==0 :

                            n+=1
                            flowerbed[i] =1
                            i+=1
                            #print("3)",i,n, ">",flowerbed)
                    else:
                        i+=2
                else:
                    if flowerbed[i+1]==0 and flowerbed[i-1]==0 :
                        n+=1
                        flowerbed[i] =1
                        i+=1
                        #print("4.1)",i,n, ">",flowerbed)
                    else:
                        i+=1
                        #print("4.2)",i,n, ">",flowerbed)
                                               
        if n>= sol:
            return True
        else :
            return False
                
            
        