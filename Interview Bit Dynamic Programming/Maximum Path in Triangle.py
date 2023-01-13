class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        for i in range(n - 2, -1, -1):
            for j in range(0, i + 1):
                A[i][j] = max(A[i + 1][j], A[i + 1][j + 1]) + A[i][j]

        return A[0][0]
