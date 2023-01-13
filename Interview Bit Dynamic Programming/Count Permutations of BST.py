from math import factorial as f
def C(n, k):
    return f(n) // f(k) // f(n - k)

values = {}

def B(n, k):
    if n < 2:
        if k < n:
            return 0
        else:
            return 1

    if (n, k) in values:
        return values[(n, k)]

    s = 0
    for r in range(n):
        s += C(n - 1, r) * B(r, k - 1) * B(n - 1 - r, k - 1)

    values[(n, k)] = s
    return s

def solution(n, k):
    return B(n, k) - B(n, k - 1)

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def cntPermBST(self, A, B):
        return solution(A, B + 1) % (10**9 + 7)
