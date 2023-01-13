'''
class Solution:
    # @param A : list of strings
    # @return a list of list of integers
    def queenAttack(self, A):
        ans = [[0 for i in range(len(A[0]))] for j in range(len(A))]

        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == '1':
                    x_cord = [1, 1, 1, -1, -1, -1, 0, 0]
                    y_cord = [1, -1, 0, 1, -1, 0, -1, 1]

                    for k in range(8):
                        x = i + x_cord[k]
                        y = j + y_cord[k]
                        while 0<=x<len(A) and 0<=y<len(A[0]):
                            ans[x][y] += 1
                            if A[x][y] == '1':
                                break;

                            x += x_cord[k]
                            y += y_cord[k]

        return ans
'''

from collections import defaultdict


class Solution:
    # @param A : list of strings
    # @return a list of list of integers
    def queenAttack(self, A):
        ans = [[0 for i in range(len(A[0]))] for j in range(len(A))]
        hasTop = [0] * len(A[0])
        hasDiag = defaultdict(int)
        hasRDiag = defaultdict(int)

        # starting from top left to bottom right
        for i in range(len(A)):
            hasleft = 0
            for j in range(len(A[0])):
                ans[i][j] = hasleft + hasTop[j] + hasDiag[j - i] + hasRDiag[j + i]
                if A[i][j] == '1':
                    hasleft = 1
                    hasTop[j] = 1
                    hasDiag[j - i] = 1
                    hasRDiag[j + i] = 1

        hasTop = [0] * len(A[0])
        hasDiag = defaultdict(int)
        hasRDiag = defaultdict(int)

        for i in range(len(A) - 1, -1, -1):
            hasright = 0
            for j in range(len(A[0]) - 1, -1, -1):
                ans[i][j] += hasright + hasTop[j] + hasDiag[j - i] + hasRDiag[j + i]
                if A[i][j] == '1':
                    hasright = 1
                    hasTop[j] = 1
                    hasDiag[j - i] = 1
                    hasRDiag[j + i] = 1

        return ans

