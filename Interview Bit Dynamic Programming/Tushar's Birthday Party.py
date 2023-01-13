class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def solve(self, friends, capacity, price):
        goal = max(friends)
        dp = [0] + [float("inf")] * goal

        for cap, pr in zip(capacity, price):
            for i in range(cap, goal + 1):
                cand_price = dp[i - cap] + pr
                if cand_price < dp[i]:
                    dp[i] = cand_price

        return sum(dp[friend] for friend in friends)
