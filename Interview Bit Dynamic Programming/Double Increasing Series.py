class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        dp = [i for i in range(1, A + 1)]

        for curr in range(2, B + 1):
            dp1 = [0 for i in range(A)]

            # dp1[0] = dp[0]+1

            for i in range(1, A):
                dp1[i] = (dp1[i - 1] + dp[(i - 1) // 2]) % 1000000007
            dp = dp1
        return dp[-1]




