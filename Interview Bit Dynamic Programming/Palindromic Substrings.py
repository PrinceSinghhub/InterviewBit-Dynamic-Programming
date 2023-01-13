class Solution:
    # @param A : string
    # @return an integer
    def solve(self, s):
        dp = [[0 for i in range(len(s))] for j in range(len(s))]

        res = 0

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if i == j:
                    dp[i][j] = 1
                elif i == j - 1 and s[i] == s[j]:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]

                if (dp[i][j] == 1):
                    res += 1

        return res
