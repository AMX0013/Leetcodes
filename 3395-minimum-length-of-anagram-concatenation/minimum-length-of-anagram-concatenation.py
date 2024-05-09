class Solution:
    

    def minAnagramLength(self, s: str) -> int:
        n = len(s)
        res = len(s)

        def check(seg_len):
            anagram = sorted(s[:seg_len])
            # print("Testing for the anagram",str(anagram))
            
            for i in range(seg_len,n,seg_len):
                word =  sorted(s[i:i+seg_len])
                if anagram != word:
                    # print("failed for: ", str(word))
                    return False                    
            return True

        for seg_len in range(1,n//2 +1 ):
            if n%seg_len != 0:
                continue
            if check(seg_len):
                return seg_len
            
        # s is the min anagram
        return res
        