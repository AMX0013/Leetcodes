class Solution:
    def reorganizeString(self, s: str) -> str:

        # fmap = {}
        # for char in s:
        #     fmap[char] = fmap.get(char,0)+1

        # print(fmap)
        
        # We use Counter , a python datastructure to create the above stuff
        count = Counter(s) 
        # now we create a heap using the char and frequencies 
        maxHeap = [ [ -cunt,char] for char , cunt in count.items() ]
        # gen heap
        heapq.heapify(maxHeap) 

        # this obj is a heap obj
        # it contains 
        lastUsed = None

        res = ""


        while lastUsed or maxHeap:

            # Finally , stopping condition:
            # If we have a lastUsed populated but our maxHeap is empty:
                # That iss: We out of charactes to pad in between

            if lastUsed and not maxHeap:
                # print("Killed:",res)
                return "" 


            # pop a character 
            count , char = heapq.heappop(maxHeap)
            # print(count,char)
            # notee: count is negative rep of the actual count inorder to represent maxHeap

            # append most freqChar into string
            res+=char
            count+=1 #to decrement it towards 0


            # only re-add popped after another element is popped

            # or u can say,
            # IFF there already exists a lastUsed , then add that back and then set it to NONE
            if lastUsed:
                heapq.heappush(maxHeap,lastUsed)
                lastUsed = None

            # then you may store current contents into last used

            # if count == 0 : cant re-add
            if count !=0:
                lastUsed = [count,char]

        return res