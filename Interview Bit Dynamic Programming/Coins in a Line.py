class Solution:
    # @param A : list of integers
    # @return an integer
    def maxcoin(self, A):
        '''
        Solution by dynamic programming.
           dp[i][j] = maximum score possible for current player for subgame A[i:j]
        Base cases, only one option:
           dp[i][i+1] = A[i]
        Otherwise, we pick at either end, eventually getting
        all the coins but the ones picked by next player:
           dp[i][j] = sum(A[i:j]) - min(dp[i+1][j], dp[i][j-1])

        Now, we only have to maintain one column (j-1) to ozzbtain new one (j).

        Time: O(n**2)   Space: O(n)
        '''

        n = len(A)
        dp = [None] * n

        for j in range(1, n + 1):
            dp[j - 1] = A[j - 1]  # dp[j-1][j]
            total = A[j - 1]
            # dp[i+1][j] must be already computed, so we iterate backward
            for i in range(j - 2, -1, -1):
                total += A[i]  # sum[i:j]
                dp[i] = total - min(dp[i + 1], dp[i])

        return dp[0]
