class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        rows, cols = len(A), len(A[0])
        for r, row in enumerate(A):
            for c, x in enumerate(row):
                if x == 1 and r > 0: A[r][c] = A[r - 1][c] + 1

        area = 0
        from collections import Counter
        for row in A:  # better: cnt histogram, then sort: T(rows * cols) ???
            length = 0
            for height, cnt in sorted([(h, c) for h, c in Counter(row).items()], reverse = True):
                length += cnt
                tmp = height * length
                if area < tmp: area = tmp
        return area

