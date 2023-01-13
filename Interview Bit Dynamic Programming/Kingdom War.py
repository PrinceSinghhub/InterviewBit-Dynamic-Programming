class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        A.insert(0, [0 for i in range(len(A[0]))])
        rows, cols = len(A), len(A[0])
        ans = -200
        for r in range(rows - 1, 0, -1):
            res = A[r][cols - 1]
            A[r - 1][cols - 1] += A[r][cols - 1]
            for c in range(cols - 2, -1, -1):
                A[r - 1][c] += A[r][c]
                if A[r][c] <= 0:
                    break
                else:
                    res += A[r][c]
            ans = max(ans, res)

        return ans

    # Time --> O(M*N); Space --> O(1)




