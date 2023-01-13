class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return a list of integers
    def solve(self, A, B, C, D):
        P = [A, B, C]
        P = sorted(P)
        import heapq
        h = []
        heapq.heappush(h, 1)
        c = 0
        r = []
        rs = set()
        x = heapq.heappop(h)
        for y in P:
            heapq.heappush(h, x * y)
        while(c < D):
            x = heapq.heappop(h)
            if x not in rs:
                rs.add(x)
                r.append(x)
                c += 1
                for y in P:
                    heapq.heappush(h, x*y)
        return r


