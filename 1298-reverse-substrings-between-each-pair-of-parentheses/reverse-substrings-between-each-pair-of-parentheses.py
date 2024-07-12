class Solution:
    def reverseParentheses(self, s: str) -> str:
        print(s)
        loc_stack = []
        idx = 0
        while idx < len(s):
            if s[idx] == '(':
                loc_stack.append(idx)
            if s[idx] == ')':
                left = loc_stack.pop()
                left+=1
                right = idx 
                rev = s[left:right][::-1]
                print(s[:left-1] , rev,  s[right+1:])
                s = s[:left-1] + rev +  s[right+1:]
                # fix idx pos to adjust for removal of ( and )
                idx -=2
                # print(s)
            idx +=1

        return s