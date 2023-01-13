from functools import lru_cache

class Solution:
    def regex_helper(self,A,B,m,n):
        if m < 0 and n < 0: return 1
        if m < 0 and n >= 0: return 0
        if m >= 0 and n < 0: return 0
        if B[n] != '*':
            if not B[n] in ['.', A[m]]:
                return 0
            else:
                return self.regex_helper(A,B,m-1,n-1)
        # if n == 0: return 0
        if B[n-1] == '.':
            return 1
        else:
            if A[m] != B[n-1]:
                return self.regex_helper(A,B,m,n-2)
            while A[m] == B[n-1]:
                if m == 0: return 1
                m -= 1
            return self.regex_helper(A,B,m,n-2)

    # @param s : string
    # @param p : string
    # @return an integer
    def isMatch(self, s, p):
        return self.regex_helper(s,p,len(s)-1,len(p)-1)
