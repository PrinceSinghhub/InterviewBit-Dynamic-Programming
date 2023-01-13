class Solution:
    # @param A : list of list of integers
    # @return an integer
    def calculateMinimumHP(self, A):

        n = len(A)
        m = len(A[0])

        dp = [[2**31 for i in range(m+1)] for j in range(n+1)]

        dp[n-1][m] = 1
        dp[n][m-1] = 1

        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                temp = min(dp[i][j+1],dp[i+1][j])-A[i][j]
                dp[i][j] = 1 if temp<=0 else temp

        return dp[0][0]
