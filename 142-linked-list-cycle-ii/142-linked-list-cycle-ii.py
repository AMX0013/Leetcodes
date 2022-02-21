# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None or head.next.next == None:
            return None
        base = head
        looper = head.next
        
        resArr = []
        loopArr = []
        
        loopCount = 0
        
         
        
        while base.next != None and looper.next != None and looper.next.next != None :
            #orderDict[base][looper] = dictIter
            temp = []
            temp.append(base)
            temp.append(looper)
            resArr.append(temp)
            print("appended :",base.val,"looper.val",looper.val)
            
            
            if base != looper:
                
                base = base.next
                looper = looper.next.next
                
            elif base == looper:
                
                base = base.next
                looper = looper.next.next
                
                while base.next != None and looper.next != None and looper.next.next != None :
                    temp = []
                    temp.append(base)
                    temp.append(looper)
                    loopArr.append(temp)
                    
                    print("InnerWhile before append :","appended :",base.val,"looper.val",looper.val)
                    
                    
                    loopCount+=1
                    if base == looper:
                        
                        break
                        
                
                    else:
                                                
                        base = base.next
                        looper = looper.next.next
                
                for left in range(0,loopCount):
                    if resArr[left] == loopArr[left]:
                        if left == 0:
                            return head
                        
                        while left >0:
                            head = head.next
                            left-=1
                        return head
                    
                        
                    
                    
                
                '''        
                resCount = len(resArr) - (2*(loopCount))
                print(" >(lenCheck) :",lenCheck," >len(resArr) :",len(resArr)," >loopCount",loopCount,resCount)
                
                  
                print(" >len(resArr) :",len(resArr)," >loopCount",loopCount)
                print("yes loop")
                break
                '''
                
                
        return None
                
        
        
        
        