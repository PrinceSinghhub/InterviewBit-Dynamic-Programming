class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # Try and do dp for it, but it will be N*3
        n = len(A)
        if n <= 1:
            return 0
        dp = [[0]*n for _ in range(n)]

        # Also pre-compute sums, as they will be needed often
        sums = [0]*n
        for i in range(n):
            sums[i] = sums[i - 1] + A[i]

        for delta in range(1,n):
            for start in range(n - delta):
                end = start + delta
                dp[start][end] = sums[end] - (sums[start - 1] if start else 0)
                dp[start][end] += min(dp[start][k] + dp[k + 1][end] for k in range(start, end))

        return dp[0][n - 1]






















