from collections import defaultdict


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def solve(self, a):
        sol = defaultdict(int)

        n = len(a)
        for i in range(n):
            for j in range(i):
                d = a[i] - a[j]
                sol[(i, d)] = max(sol[(i, d)], 1 + sol[(j, d)])

        return max(sol.values(), default=0) + 1


