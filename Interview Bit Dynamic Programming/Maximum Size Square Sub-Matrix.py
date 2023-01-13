class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        n, m = len(A), len(A[0])
        prev = A[0] + []
        currmax = max(prev)
        curr = [0] * m
        for i in range(1, n):
            curr[0] = A[i][0]
            for j in range(1, m):
                if A[i][j] == 0:
                    curr[j] = 0
                else:
                    curr[j] = 1 + min(curr[j - 1], prev[j - 1], prev[j])
            currmax = max(currmax, max(curr))
            prev, curr = curr, prev

        return currmax * currmax
