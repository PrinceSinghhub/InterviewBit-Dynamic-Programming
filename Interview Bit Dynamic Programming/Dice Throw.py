class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def findDiceSum(self, A, B, C):
        dp = [0] * (C + 1)
        dp[0] = 1

        for i in range(1, A + 1):
            dp_new = [0] * (C + 1)
            last = min((B * i), C)
            for j in range(i, min(B + i, C + 1)):
                dp_new[j] = dp_new[j - 1] + dp[j - 1]

            for j in range(B + i, last + 1):
                dp_new[j] = dp_new[j - 1] + dp[j - 1] - dp[j - B - 1]

            dp = dp_new[:]
            # print("dp", dp)


        return dp[C] % (10 ** 9 + 7)

