class Solution:
    def trap(self, height: List[int]) -> int:
        
        water = 0
        i = 0
        
        stack = []
        while i < len(height):
            #print(i, height[i])
            
            while len(stack)!= 0 and height[ stack[len(stack)-1] ]< height[i]:
                top = stack[len(stack)-1]
                stack.pop() 
                #print("top =",top)
                if len(stack)== 0:
                    #stack.append(top)
                    break # to remove leftmost wall and the pushes wall will be the first/ leftmost wall
                nextTop = stack[len(stack)-1]
                
                #print("next  top =", nextTop)
                width= i - nextTop-1
                unFilledHeight = min( height[i] , height[nextTop]) - height[top]
                tempWater= width*unFilledHeight
                water += tempWater
                #print("width =",width,"unFilledHeight =",unFilledHeight , "tempWater =",tempWater)
                #print(stack)
                
            stack.append(i)
            #print(stack)
            i+=1
        
        
        return water
        
        
        '''if height[i+1] == height[i]:
                i+=1
            
            
            elif height[i] < height[i-1]:
                stack.append([i,height[i]]) #index, height
                i+=1
            
            elif i !=0 and height[i] > height[i-1]:
                print("water calc",i)
                tempWater = 0
                maxSolid = -1
                solidFill = 0
                if stack:

                    while stack and stack[len(stack)-1][1] <= height[i]:
                        temp = stack.pop()  #index, height
                        if temp[1] > maxSolid:
                            maxSolid = temp[1]
                        solidFill += temp[1]


                    diff = abs(i - temp[0] )
                    tempWater = (diff *  maxSolid) - solidFill

                #push this wall into stack
                stack.append([i,height[i]]) #index, height
                i+=1
            else:
                print("unknown condition", i)
                i+=1'''
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''
        #print(height)
        i = 0
        tempFill = 0        
        start = i
        end = i+1
        if height[i] == 0:
            while height[i] == 0 and i < len(height)-1:
                i+=1
        
            
        #print( i, height[i])
        water = 0
        if i >= len(height):
            return water
        # lookfor a cavity:
        
        while i < len(height)-1:
            #print("_________________________")
            start = i
            indexMaxHt = start
            maxHt = -1
            end = i
            #print("start",start)
            while end <= len(height)-2:                
                
                
                if end ==  start and height[end+1] > height[end]:
                    #print("next")
                    end+=1
                    break
                elif height[end+1] <= height[end]: # a downward slope
                    #print("down")
                    end +=1 # godown until atleast a local maxim is found
                    
                elif height[end+1] > height[end] and height[end+1] <= height[start]: #and height[end+1] >= maxHt  : #rising
                    #
                    
                    end +=1
                    if  height[end] > maxHt:
                        maxHt = height[end]
                        indexMaxHt = end
                    #print("rising",end,maxHt)
                    
                elif height[end+1] > height[start]:
                    end+=1
                    if  height[end] > maxHt:
                        maxHt = height[end]
                        indexMaxHt = end
                    break
            
            #print("end = " , end)            
            if end >= len(height)-1 and maxHt != -1 :
                end = indexMaxHt
            
            i = end
            maxHt =  min(maxHt,height[start])
            
            if  maxHt != -1 :

                # water is filled up till the shorter height 
                #print("end - start -1 =  " , diff, "maxht", maxHt)

                tempFill = 0 #diff * maxHt
                for bar in range(start+1,end):
                    if height[bar] < maxHt:
                        #print("index>",bar,"ht>", height[bar] )
                        tempFill += maxHt - height[bar]
                water += tempFill

                #print ("end>",end,"tempFill>", tempFill)
            
            
            #print("_________________________")
            
        return water
        '''    
                    
                    
                    
        