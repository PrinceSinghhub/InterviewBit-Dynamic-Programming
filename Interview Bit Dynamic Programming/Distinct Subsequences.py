class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def numDistinct(self, A, B):
        d = {}
        def rec(p1, p2):
            if p2 > p1:
                return 0
            elif p2 == -1:
                return 1
            if (p1, p2) not in d:
                if A[p1] == B[p2]:
                    d[(p1, p2)] = rec(p1 - 1, p2 - 1) + rec(p1 - 1, p2)
                else:
                    d[(p1, p2)] = rec(p1 - 1, p2)
            return d[(p1, p2)]
        return rec(len(A)-1, len(B)-1)

