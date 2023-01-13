class Solution:
    # @param A : string
    # @return an integer
    def cnttrue(self, A):
        n = len(A)//2+1
        dp = [[[0, 0] for j in range(n)] for i in range(n)]
        for i in range(0, len(A), 2):
            dp_i = i//2
            if A[i] == 'T':
                dp[dp_i][dp_i][0] = 1
            else:
                dp[dp_i][dp_i][1] = 1
        for l in range(2, n+1):
            for i in range(n-l+1):
                j = i+l-1
                max_t, max_f = 0, 0
                for k in range(i, j):
                    left_t, left_f = dp[i][k]
                    right_t, right_f = dp[k+1][j]
                    op = A[k*2+1]
                    if op == '|':
                        max_t += (left_t * right_t + left_t * right_f + left_f * right_t)
                        max_f += (left_f * right_f)
                    elif op == '&':
                        max_t += (left_t * right_t)
                        max_f += (left_t * right_f + left_f * right_f + left_f * right_t)
                    elif op == '^':
                        max_t += (left_t * right_f + left_f * right_t)
                        max_f += (left_t * right_t + left_f * right_f)
                dp[i][j] = [max_t, max_f]
        # print(dp)
        return dp[0][n-1][0] % 1003
