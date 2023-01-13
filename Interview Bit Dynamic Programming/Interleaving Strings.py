class Solution:
    # @param A : string
    # @param B : string
    # @param C : string
    # @return an integer
    def isInterleave(self, A, B, C):

        from functools import lru_cache

        cache = dict()

        def dp(i, j, k):
            if k < 0:
                if i >= 0 or j >= 0:
                    return False
                return True

            if i < 0 and j < 0: return 1
            if i < 0:
                return 1 if C[:k] == B[:j] else 0
            if j < 0:
                return 1 if C[:k] == A[:i] else 0

            if (i, j, k) in cache:
                return cache[(i, j, k)]

            if C[k] == A[i]:
                if (i - 1, j, k - 1) in cache:
                    t1 = cache[(i - 1, j, k - 1)]
                else:
                    t1 = dp(i - 1, j, k - 1)
                    cache[(i - 1, j, k - 1)] = t1

                if A[i] != B[j]:
                    return t1
                else:
                    if (i - 1, j, k - 1) in cache:
                        t2 = cache[(i - 1, j, k - 1)]
                    else:
                        t2 = dp(i - 1, j, k - 1)
                        cache[(i - 1, j, k - 1)] = t2
                    if (i, j - 1, k - 1) in cache:
                        t3 = cache[(i, j - 1, k - 1)]
                    else:
                        t3 = dp(i, j - 1, k - 1)
                        cache[(i - 1, j, k - 1)] = t3

                    return t2 or t3
            elif C[k] == B[j]:
                if A[i] != B[j]:
                    if (i, j - 1, k - 1) in cache:
                        t4 = cache[(i, j - 1, k - 1)]
                    else:
                        t4 = dp(i, j - 1, k - 1)
                        cache[(i, j - 1, k - 1)] = t4

                    return t4
                else:
                    if (i - 1, j, k - 1) in cache:
                        t2 = cache[(i - 1, j, k - 1)]
                    else:
                        t2 = dp(i - 1, j, k - 1)
                        cache[(i - 1, j, k - 1)] = t2
                    if (i, j - 1, k - 1) in cache:
                        t3 = cache[(i, j - 1, k - 1)]
                    else:
                        t3 = dp(i, j - 1, k - 1)
                        cache[(i - 1, j, k - 1)] = t3

                    return t2 or t3

            return 0

        return dp(len(A) - 1, len(B) - 1, len(C) - 1)





