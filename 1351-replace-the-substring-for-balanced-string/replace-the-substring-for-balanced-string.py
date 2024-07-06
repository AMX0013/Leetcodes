class Solution:
    def balancedString(self, s: str) -> int:
        N = len(s)
        s_map = Counter(s)
        min_substr_len = N
        
        # The target count for each character
        target = N // 4
        L = 0
        
        def valid(s_map):
            for key in 'QWER':
                if s_map[key] > target:
                    return False
            return True
        
        for R in range(N):
            s_map[s[R]] -= 1
            
            while valid(s_map):
                min_substr_len = min(min_substr_len, R - L + 1)
                s_map[s[L]] += 1
                
                if L<N-1:
                    L += 1
        
        return min_substr_len