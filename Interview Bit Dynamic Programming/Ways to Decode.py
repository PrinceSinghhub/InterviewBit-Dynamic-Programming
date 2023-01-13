class Solution:
    # @param A : string
    # @return an integer
    def numDecodings(self, A):
        m = len(A)
        if len(A) == 0: return 0
        if len(A) == 1:
            if int(A) >= 1 and int(A) <= 9:
                return 1
            else:
                return 0
        if len(A) == 2:
            if A in ['10', '20']:
                return 1
            elif A[-1] != '0' and int(A) < 27:
                return 2
            else:
                return 1
        if A.startswith('0'): return 0
        dp = [0 for i in range(0, m)]
        dp[0] = 1
        for i in range(1, len(A)):
            n = int(A[i - 1]) * 10 + int(A[i])

            if int(A[i]) >= 1 and int(A[i]) <= 9:
                dp[i] = dp[i - 1]

            if n >= 1 and n <= 26 and int(A[i - 1]) > 0:
                if i > 1:
                    dp[i] += dp[i - 2]
                else:
                    dp[i] += 1
        return dp[m - 1]
