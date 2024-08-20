class Solution:
    def validStrings(self, n: int) -> List[str]:
        # create a string representing a binary value
        # it should be of length n

        # rule: all substring of length 2 should contain a "1"

        # create all strings of length n, valid to this rule
        memo = defaultdict()

        def fwd(pre:str, len_left:int):
            if (pre,len_left) in memo:
                # print("from memo, pre:",pre, "len_left:",len_left, "yielded:", memo[(pre,len_left)])
                return memo[(pre,len_left)]
            res = set()
            if len_left ==0:
                # print("A Pre:", pre )
                return {pre}
            else:
                if len(pre)>0 and pre[-1] == "0":
                    res.update(  fwd( pre + "1" , len_left-1 ) )                
                else:
                    res.update(  fwd( pre + "0" , len_left-1 ) )                
                    res.update(  fwd( pre + "1" , len_left-1 ) )         
            memo[(pre,len_left)] = res
            # print("from compute, pre:",pre, "len_left:",len_left, "yielded:", memo[(pre,len_left)] )  

            return res

        return list(fwd("",n))
