class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        s = list(s)
        # print(s)
        out = []
        for idx, c in enumerate(s):
            # print(idx,"rotated idx: ",(idx+k)%len(s))
            out.append(s[ (idx+k)%len(s) ]) 
            # print(out)
        
        return "".join(out)