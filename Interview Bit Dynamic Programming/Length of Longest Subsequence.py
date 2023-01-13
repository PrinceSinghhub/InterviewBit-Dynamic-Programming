class Solution:
    # @param A : tuple of integers
    # @return an integer

    def longestSubsequenceLength(self, A):
        if not A: return 0

        from bisect import bisect_left
        dp = [0 for i in range(len(A))]

        arr = []

        for i in range(len(A)):
            idx = bisect_left(arr, A[i])
            dp[i] = idx
            try:
                arr[idx] = (A[i])
            except:
                arr.append(A[i])

        arr.clear()

        for i in range(len(A) - 1, -1, -1):
            idx = bisect_left(arr, A[i])
            dp[i] += idx
            try:
                arr[idx] = (A[i])
            except:
                arr.append(A[i])

        return max(dp) + 1
