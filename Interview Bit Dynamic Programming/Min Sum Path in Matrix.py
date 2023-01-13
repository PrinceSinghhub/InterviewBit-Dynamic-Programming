class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minPathSum(self, A):
        if not A:
            return 0

        n, m = len(A), len(A[0])

        dp = [[0] * m for _ in range(n)]

        dp[0][0] = A[0][0]

        for j in range(1, m):
            dp[0][j] = dp[0][j - 1] + A[0][j]

        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + A[i][0]

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + A[i][j]

        return dp[-1][-1]

