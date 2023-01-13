class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        if not A or not A[0]: return 0  # SC & guard

        cols = len(A[0]) + 1            # pad left to guard [c - 1]
        A = [[0] + row for row in A]
        for row in A:                   # prefix sum each row
            for c in range(2, cols):
                row[c] += row[c - 1]

        zeros = 0
        for c1 in range(cols - 1):                  # each pair of (c, c2]
            for c2 in range(c1 + 1, cols):
                sofar = 0
                seen = {0: 1}                   # {sum : cnt}, dict to cnt dups
                for row in A:                   # scan top-down as 1D sum 0
                    sofar += row[c2] - row[c1]
                    if sofar in seen:
                        zeros += seen[sofar]
                        seen[sofar] += 1
                    else: seen[sofar] = 1
        return zeros

