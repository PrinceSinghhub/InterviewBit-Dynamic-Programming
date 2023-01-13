import sys


class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def rodCut(self, rod_length, cuts):
        def bnd(i):
            if i == 0:
                return 0
            if i == len(cuts) + 1:
                return rod_length
            return cuts[i - 1]

        def backtrack(T, row, col):
            if col - row <= 1:
                return []
            cut_point = T[row][col]
            result = [bnd(cut_point)]
            result.extend(backtrack(T, row, cut_point))
            result.extend(backtrack(T, cut_point, col))
            return result

        size = len(cuts) + 2
        M = [[0] * size for n in range(size)]
        N = [[-1] * size for n in range(size)]

        for i in range(2, size):
            for j in range(0, size - i):
                row = j
                col = i + j
                min_c = sys.maxsize
                min_index = sys.maxsize
                rod_cost = bnd(col) - bnd(row)
                for k in range(row + 1, col):
                    cost = M[row][k] + M[k][col]
                    if cost < min_c:
                        min_c = cost
                        min_index = k
                M[row][col] = min_c + rod_cost
                N[row][col] = min_index

        return backtrack(N, 0, size - 1)
