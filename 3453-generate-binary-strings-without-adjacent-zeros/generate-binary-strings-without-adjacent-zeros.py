class Solution:
    def validStrings(self, n: int) -> List[str]:
        # create a string representing a binary value
        # it should be of length n

        # rule: all substring of length 2 should contain a "1"

        # create all strings of length n, valid to this rule

        if n==1:return ['0','1']
        valid=['0','1']
        for _ in range(n-1):
            new=[]
            for s in valid:
                if s[-1]=='1':
                    new.append(s+'0')
                    new.append(s+'1')
                else:
                    new.append(s+'1')
            valid=new
        
        return valid

        # memo: Dict[Tuple[int, str], List[str]] = {}

        # def backtrack(remaining: int, last_char: str) -> List[str]:
        #     if remaining == 0:
        #         return [""]  # Base case: a valid string of length 0 is an empty string

        #     if (remaining, last_char) in memo:
        #         return memo[(remaining, last_char)]

        #     res = []
        #     # If the last character is '0', we must append '1'
        #     if last_char == "0":
        #         for next_str in backtrack(remaining - 1, "1"):
        #             res.append("1" + next_str)
        #     else:
        #         # The last character is '1', we can append either '0' or '1'
        #     # else last_char == "1":
        #         for next_str in backtrack(remaining - 1, "0"):
        #             res.append("0" + next_str)
        #         for next_str in backtrack(remaining - 1, "1"):
        #             res.append("1" + next_str)

        #     memo[(remaining, last_char)] = res
        #     return res

        # # Start the backtracking with initial calls
        # return backtrack(n , "")
