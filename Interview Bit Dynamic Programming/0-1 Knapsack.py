class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer

    def solve(self, A, B, C):
        n = len(B)  # number of items
        dp = [0] * (C + 1)  # value at C j Space(C)
        items = set()  # B contribute to dpJnWi > dp[j]
        for i in range(
                n):  # Time(N*C) for each item weight, iterate from C to this item weight, find the max value including this item
            for j in range(C, B[i] - 1, -1):  # -1 to include B[0]
                dpJnWi = A[i] + dp[j - B[i]]  # value of i + value at C j less B[i]
                if dpJnWi > dp[j]:  # before: value at C j without i because "for j loop" starting at full C
                    dp[j] = dpJnWi  # after: including A[i]
                    if sum(items) + B[i] <= C:
                        items.add(B[i])
        return dp[C]
