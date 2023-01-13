class Solution:
    # @param A : list of list of integers
    # @return an integer
    def adjacent(self, grid):
        incl = max(grid[0][0], grid[1][0])
        excl = 0

        for i in range(1, len(grid[0])):
            excl_new = max(excl, incl)

            incl = excl + max(grid[0][i], grid[1][i])

            excl = excl_new

        return max(incl, excl)

