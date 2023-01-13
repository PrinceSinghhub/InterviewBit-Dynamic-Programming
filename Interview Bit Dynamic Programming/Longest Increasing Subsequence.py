from functools import lru_cache


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        n = len(A)

        @lru_cache(None)
        def _helper(idx):
            if idx == n - 1:
                return 1
            ans = 1
            for i in range(idx + 1, n):
                if A[i] > A[idx]:
                    ans = max(ans, _helper(i) + 1)
            return ans

        out = 1
        for i in range(n):
            out = max(out, _helper(i))

        return out