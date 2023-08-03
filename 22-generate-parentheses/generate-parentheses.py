class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        currCombo = []
        res = []

        def recur(openCount,closeCount):
            if openCount==closeCount==n:
                res.append("".join(currCombo))
                return

            if openCount < n:
                currCombo.append("(")
                # openCount+=1
                recur(openCount+1,closeCount)
                currCombo.pop()

            if closeCount < openCount:
                currCombo.append(")")
                # openCount+=1
                recur(openCount,closeCount+1)
                currCombo.pop()
        recur(0,0)

        return res

                    