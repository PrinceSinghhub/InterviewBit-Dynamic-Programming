class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, a, b):
        n = b
        m = len(a)

        if n >= m / 2:
            return sum((a[i + 1] - a[i]) for i in range(len(a) - 1) if a[i + 1] > a[i])

        dp = [0] * (m + 1)
        dpmax = [-float('inf')] * (m + 1)
        dpmax_t = [-float('inf')] * (m + 1)

        for i in range(m):
            dpmax[i + 1] = max(dpmax[i], -a[i])
            dpmax_t[i + 1] = max(dpmax_t[i], -a[i])

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[j] = max(dp[j - 1], a[j - 1] + dpmax[j - 1])
                dpmax_t[j] = max(dpmax_t[j - 1], -a[j - 1] + dp[j])

            dpmax, dpmax_t = dpmax_t, dpmax

        # print(dp)
        # print(dpmax)

        return dp[m]
