class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)

        leftover_chalk = k%total

        for i in range(len(chalk)):
            if leftover_chalk < chalk[i]:
                return i
            else:
                leftover_chalk -= chalk[i]
                
        