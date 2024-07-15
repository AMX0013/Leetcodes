class Solution:
    def compress(self, chars: List[str]) -> int:
        printr =0 #an idx that starts writing the res on top of chars
        # only uptil this loc after all computation, the res is coheerent. 
        # fter that, the original chars arr elements exist
        R= 0
        
        while R < len(chars):
            ref = chars[R]
            count = 0
            # starts in place adha
            while R<len(chars) and chars[R] == ref:
                count+=1
                R+=1
            
            # start printing resultant arr into chars
            
            chars[printr] = ref
            printr +=1
            if count >1:
                for digit in str(count):
                    chars[printr] = digit
                    printr +=1

        print("fulllasss",chars)
        
        return printr

        

        