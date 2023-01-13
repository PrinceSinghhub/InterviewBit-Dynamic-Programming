class Solution:
    # @param A : string
    # @return an integer
    def minCut(self, A):
        self.palins = self.find_all_palindromes(A)
        self.dp = {}
        return self.num_ways_if_cut_here(0, A)

    def num_ways_if_cut_here(self, i, A):
        if i >= len(A):
            return 0
        if i in self.dp:
            return self.dp[i]
        mn = math.inf
        for j in self.palins[i]:
            if j == len(A) - 1:
                return 0
            mn = min(mn, 1 + self.num_ways_if_cut_here(j + 1, A))
        self.dp[i] = mn
        return self.dp[i]

    def find_all_palindromes(self, A):
        palins = {}
        for center in range(len(A)):
            self.get_palins_with_center(center, A, palins)
        return palins

    def get_palins_with_center(self, center, A, palins):
        # Odd
        i = center
        j = center
        palins[i] = []
        while 0 <= i and j < len(A) and A[i] == A[j]:
            palins[i].append(j)
            i -= 1
            j += 1
        # Even
        if center >= len(A) - 1:
            return
        i = center
        j = center + 1
        while 0 <= i and j < len(A) and A[i] == A[j]:
            palins[i].append(j)
            i -= 1
            j += 1
        return
