class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def findTarget(self, i, n, t, c, l, A):
        if n == 0:
            if t:
                return None
            else:
                return []
        if i >= l:
            return None
        if A[i] > t:
            return None
        if (i, n, t) in c:
            return c[(i, n, t)]
        res = self.findTarget(i + 1, n - 1, t - A[i], c, l, A)
        if res is not None:
            res = [i] + res
        else:
            res = self.findTarget(i + 1, n, t, c, l, A)

        c[(i, n, t)] = res
        return res

    def avgset(self, A):
        l, tot = len(A), sum(A)
        if l < 2:
            return []
        A = sorted(A)

        for x in range(1, l // 2 + 1):
            d, r = divmod(tot * x, l)
            if r:
                continue
            cache = {}
            res = self.findTarget(0, x, d, cache, l, A)
            if res is not None:
                A1 = [A[j] for j in res]
                A2 = [A[j] for j in range(l) if j not in res]
                return [A1, A2]
        return []




