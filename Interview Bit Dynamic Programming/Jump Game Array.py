class Solution:
    # @param A : list of integers
    # @return an integer
    def canJump(self, A):
        count = 0

        for i, a in enumerate(A):
            if i > count:
                return 0
            count = max(count, i + a)

        return 1