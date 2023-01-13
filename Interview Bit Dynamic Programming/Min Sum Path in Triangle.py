class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minimumTotal(self, A):
        n = len(A)
        temp = [A[-1][j] for j in range(n)]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                temp[j] = A[i][j] + min(temp[j], temp[j + 1])

        return temp[0]

