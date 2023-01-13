class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProduct(self, A):
        assert len(A) > 0
        ans = A[0]
        ma, mi = 1, 1
        for a in A:
            ma, mi = max(a, a * ma, a * mi), min(a, a * ma, a * mi)
            ans = max(ans, ma, mi)
        return ans

