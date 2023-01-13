class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if (A % 2): return 0
        complete = 1
        partial = 1
        for i in range(2, A + 1, 2):
            complete = (complete + 2 * partial) % (10 ** 9 + 7)
            partial = (complete + partial) % (10 ** 9 + 7)
        return complete

