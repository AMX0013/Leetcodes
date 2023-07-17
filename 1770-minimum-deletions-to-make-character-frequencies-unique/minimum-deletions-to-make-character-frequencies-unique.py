class Solution:
    def minDeletions(self, s: str) -> int:
        charFreqMap = defaultdict(int)
        
        maxFreq  = 0
        deletions = 0
        allocated = 0
        totalDeletions = 0
        for char in s:
            charFreqMap[char]=charFreqMap.get(char,0)+1
            maxFreq = max(maxFreq,charFreqMap[char] )
        # print(maxFreq)
        
        # InvertedDict

        freq_char_map = defaultdict()
        
        for char, freq in charFreqMap.items():
            if freq in freq_char_map:
                freq_char_map[freq].append(char)
                totalDeletions += freq
            else:
                freq_char_map[freq] =[char]
        
        for i in range(maxFreq,-1,-1):
            if i not in freq_char_map.keys():
                freq_char_map[i] = list()
        # print(freq_char_map)

        # 2 pointers:
        for freqKey in range(maxFreq,-1,-1):

            while len( freq_char_map[freqKey] ) >1:

                char = freq_char_map[freqKey].pop()

                downwardFreqAllocator = freqKey-1
                print("popped :", char, "No . of characters present now = ",freqKey)
                while downwardFreqAllocator >=0:
                    print("trying permissible freq : ", downwardFreqAllocator)
                    if downwardFreqAllocator == 0:
                        print("totalDeletions :",totalDeletions,"allocated",allocated)
                        return totalDeletions-allocated

                    if len(freq_char_map[downwardFreqAllocator] )== 0:
                        # print("Found permissble freq :", downwardFreqAllocator)
                        freq_char_map[downwardFreqAllocator].append(char)
                        # print(freq_char_map[downwardFreqAllocator])
                        deletions += (freqKey - downwardFreqAllocator ) 
                        allocated += downwardFreqAllocator
                        break
                    downwardFreqAllocator -=1
        # print(freq_char_map)
        

        return deletions


