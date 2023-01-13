import heapq


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        n, m = len(B), len(B[0])

        max_list = []

        for i in range(n):
            for j in range(m): heapq.heappush(max_list, (-B[i][j], (i, j)))

        def ind_gen(index, k):
            i0, j0 = index
            indices = []
            for i in range(max(0, i0 - k), min(n, i0 + k + 1)):
                # print(i0,max(0,i0-k),min(n,i0+k+1))
                d = abs(i - i0)
                for j in range(max(0, j0 - (k - d)), min(m, j0 + (k - d) + 1)):
                    indices.append((i, j))
            return indices

        index_set = set()

        while len(index_set) < n * m:
            max_val, curr_index = heapq.heappop(max_list)
            max_val *= -1

            indices = ind_gen(curr_index, A)
            for index in indices:
                if index not in index_set:
                    B[index[0]][index[1]] = max_val
                    index_set.add(index)

        return B



