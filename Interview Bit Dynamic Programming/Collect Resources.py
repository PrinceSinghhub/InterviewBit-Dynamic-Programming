class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):

        dp = [0] * 1005
        mx = [0] * 1005

        ans = 0
        s = 0
        r = len(A)
        c = len(A[0])
        for i in range(r):
            for j in range(c):
                ans += A[i][j]

        for i in range(r):
            for j in range(c):
                B[i][j] -= A[i][j]

        dp[0] = 0
        mx[0] = 0
        for i in range(1, c + 1):
            s += B[0][i - 1]
            dp[i] = s
            mx[i] = max(mx[i - 1], dp[i])

        for i in range(1, r):
            dp[0] = mx[0]
            s = 0
            for j in range(1, c + 1):
                s += B[i][j - 1]
                dp[j] = s + mx[j]

            for j in range(1, c + 1):
                mx[j] = max(mx[j - 1], dp[j])

        return int((ans + mx[c]) % 1000000007)
