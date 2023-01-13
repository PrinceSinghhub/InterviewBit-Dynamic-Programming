class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        profit = 0
        if not len(A):
            return profit
        buy = A[0]
        for elem in A:
            if elem > buy:
                profit += (elem - buy)
            buy = elem

        return profit
