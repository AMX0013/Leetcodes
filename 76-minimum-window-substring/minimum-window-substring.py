class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Given anagram in the form of a hashmap
        anagramDictT = {}
        # a hashmap to represent our sliding window
        # Lets visualize our sliding window as a worm . (Helped me, think of snake or whatev (humanCentipede? ))
        wormDict = {}

        if s == t:
            return s

        res = ""
        minLen = len(s)+1
        
        
        if len(t) > len(s):
            return ""

        have = 0
        for char in t:
            
            anagramDictT[char]= anagramDictT.get(char,0)+1


        need = len(anagramDictT) 
        headRun = True

        # our worm's head and tail location
        
        tail = 0        

        for head in range(len(s)) :


            # current char c
            c = s[head]
            # eat up this char nonetheless
            wormDict[c] = 1 + wormDict.get(c,0)
            
            # If char part of src T
            if c in anagramDictT and wormDict[c] == anagramDictT[c] :
                have+=1

            # shrink worm size
            # Shrinking the substring window
            # print(have ,"==", need, have == need)
            while have == need:  
                # Agenda : # tail is to be reduced
                # note how we dont check for removing a part of substring here first
                # This is because rn, have == need : True

                # 1 take substring
                if (head-tail+1) < minLen :
                    res = s[tail:head+1]
                    # print(res)
                    minLen = (head-tail+1)
                # We are about to reduce tail, so we pop the element from our dict
                wormDict[ s[tail] ] -=1

                if s[tail]  in anagramDictT and wormDict[ s[tail] ] < anagramDictT[s[tail]]:
                    have-=1
                tail+=1


        return res 






        '''

        while tail<=len(s)-1 :

            # Step 1> Eat s[head]  if its part of anagram
            print("tail",tail,"head",head)
            print("s[tail]",s[tail],"s[head]",s[head])
            print("s[head] in anagramDictT : ",s[head] in anagramDictT)
            print("headRun",headRun)
            

            if s[head] in anagramDictT:

                if headRun == True:
                    wormDict[ s[head] ] = wormDict.get(s[head] , 0)+1

                # The tail has not moved yet
                # If in case , the tail is in a position such that
                # wormDict[ s[tail] ] > anagramDictT[ s[tail] ] , we must essentialy move tail, and remove our character from our wormDict
                print("wormDict[ ",s[tail]," ] > anagramDictT[ ",s[tail]," ] : ",wormDict[ s[tail] ] > anagramDictT[ s[tail] ] ,wormDict[ s[tail] ] ,">", anagramDictT[ s[tail] ])

                # if wormDict[ s[tail] ] > anagramDictT[ s[tail] ]:
                #     wormDict[ s[tail] ] -= 1
                #     tail+=1

                # Move tail until we reach an element that is part of the anagram
                # s[tail] not in anagramDictT is not good
                while tail <= head :
                    print("\twhile")
                    
                    # If the ingested char completes the anagram:
                    # poop it out
                    if wormDict == anagramDictT :
                        print("wormDict == anagramDictT :", wormDict == anagramDictT)
                        subRes = "".join(s[ tail : head+1 ])
                        # minimization
                        if len(subRes) < minLen:
                            minLen = len(subRes)
                            minSubWindow = subRes
                        print("subRes :",subRes , "minSubWindow" ,minSubWindow)

                        break
                        
                    if s[tail] in wormDict  and wormDict[ s[tail] ] > anagramDictT[ s[tail] ]:
                        wormDict[ s[tail] ] -= 1
                    print("\ts[",tail,"]",s[tail],"s[",head,"]",s[head])

                    tail+=1
                print("\ts[",tail,"]",s[tail],"s[",head,"]",s[head])



                
                


            print("\wormDict",wormDict)
            # If s[head] is not part of the anagram,, simply move it,
            #  but also need to make sure that tail gets to scan throught the input list, so we let head wait at the last element
            # And create a variable that stops head from running

            if head == len(s)-1:
                headRun = False

            if head < len(s)-1:
                head+=1

            # Now we must deal with tail's movement
            # It must increment by default, until a character that is part of anagram, if so, it must wait there
            while tail <= head and s[tail] not in anagramDictT:
                tail+=1 


            # Finally, if head reaches to end, only shrinking must happen

            if headRun == False:
                if wormDict[ s[tail] ] > anagramDictT[ s[tail] ]:
                    wormDict[ s[tail] ] -= 1
                tail+=1

            print("////////")
            
            
        return minSubWindow

        '''