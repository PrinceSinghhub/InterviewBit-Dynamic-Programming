class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):

        steps = [(0, 0)]
        while steps:
            row, col = steps.pop()
            go_right = len(A[row])-1 > col and A[row][col+1] > A[row][col]
            go_left = len(A)-1 > row and A[row+1][col] > A[row][col]
            path_ended = not go_right and not go_left
            if path_ended and row == len(A) - 1 and col == len(A[row]) - 1:
                return len(A)-1+len(A[row])
            else:
                if go_right:
                    steps.append((row, col+1))
                if go_left:
                    steps.append((row+1, col))
        return -1


# 2 8 35 1 70 25 79 59 63 65 6 46 82 28 62 92 96 43
# 4 4 1 2 3 4 2 2 3 4 3 2 3 4 4 5 6 7

