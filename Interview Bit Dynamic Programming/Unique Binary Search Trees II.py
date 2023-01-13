class Solution:
    # @param A : integer
    # @return an integer
    def numTrees(self, A):
        A_len = A + 1
        catalan_array = [1 for i in range(A_len)]

        for i in range(A_len):
            if i == 1 or i == 0:
                catalan_array[i] = 1
                continue

            sum = 0
            for j in range(i):
                sum = sum + catalan_array[j] * catalan_array[i - j - 1]
            catalan_array[i] = sum

        return catalan_array[A]

