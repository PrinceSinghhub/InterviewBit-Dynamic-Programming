class Solution:
    # @param A : tuple of integers
    # @return an integer

    # BruteForce:
    def maxProfit(self, A):
        gain1 = gain2 = 0
        cost1 = cost2 = float('inf')

        for price in A:
            if cost1 > price:
                cost1 = price
            elif gain1 < price - cost1:
                gain1 = price - cost1

            if cost2 > price - gain1:
                cost2 = price - gain1
            elif gain2 < price - cost2:
                gain2 = price - cost2
        return gain2



