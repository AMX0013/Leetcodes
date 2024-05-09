class Solution:
    

    def minAnagramLength(self, s: str) -> int:
        n = len(s)
        res = len(s)
        for seg_len in range(1,n ):
            if n%seg_len != 0:
                continue
            anagram = Counter(s[:seg_len])
            # print("Testing for the anagram",str(anagram))
            is_anagram = True
            # else
            for i in range(seg_len,n,seg_len):
                word =  Counter(s[i:i+seg_len])
                if anagram != word:
                    # print("failed for: ", str(word))
                    is_anagram = False
                    break
            if is_anagram:
                return seg_len
        # s is the min anagram
        return res
        