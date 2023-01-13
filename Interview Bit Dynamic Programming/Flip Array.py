import math


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def solve(self, num):
        s = sum(num)
        dp = [math.inf for x in range(int(s / 2) + 1)]
        dp[0] = 0

        for i in num:
            for j in range(int(s / 2), 0, -1):
                if j >= i:
                    dp[j] = min(dp[j], dp[j - i] + 1)

        for i in range(int(s / 2), 0, -1):
            if dp[i] != math.inf:
                return dp[i]


