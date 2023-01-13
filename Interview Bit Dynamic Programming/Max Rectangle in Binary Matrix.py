class Solution:
    # @param A : list of list of integers
    # @return an integer
    def maximalRectangle(self, A):
        cols = len(A[0]) + 1            # pad rightmost w lowest height 0, so in each row:
        A = [row + [0] for row in A]    # stack non-empty, and final flush (see 04 0084H)       !!!

        max_rectangle = 0               # global max, for answer
        prev_row = [0] * cols           # initial prev_row ~~ top padding
        for curr_row in A:
            stack = [-1]
            for right in range(cols):   # col ~~ open right boundary
                height = curr_row[right] = 0 if curr_row[right] == 0 else (1 + prev_row[right])
                while height < curr_row[stack[-1]]:         # if prev is higher: pop to process
                    curr_height = curr_row[stack.pop()]     # as it can't continue w lower
                    curr_rectangle = (right - stack[-1] - 1) * curr_height  # open left: [-1]
                    if max_rectangle < curr_rectangle: max_rectangle = curr_rectangle
                stack.append(right)
            prev_row = curr_row         # for next row
        return max_rectangle


