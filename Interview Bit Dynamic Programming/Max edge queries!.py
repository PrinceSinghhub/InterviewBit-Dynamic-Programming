class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        ans = []
        n = 0
        for i, j, _ in A:
            n = max(n, max(i, j))
        adj = [[] for i in range(n)]
        root = 0
        for i, j, k in A:
            adj[i - 1].append((j - 1, k))
            adj[j - 1].append((i - 1, k))
        parent = [None] * n
        depth = [None] * n
        stack = []
        root = 0
        stack.append(root)
        depth[root] = 1
        vis = set()
        vis.add(0)
        while stack:
            curr = stack.pop()

            for i, j in adj[curr]:
                if i != curr and i not in vis:
                    parent[i] = curr, j
                    stack.append(i)
                    vis.add(i)
                    if depth[i] is None:
                        depth[i] = depth[curr] + 1
        for i, j in B:
            i -= 1
            j -= 1
            m = None
            if depth[i] < depth[j]:
                i, j = j, i
            while depth[i] > depth[j]:
                pw, w = parent[i]
                i = pw
                if m is None or (m and m < w):
                    m = w

            while parent[i] != parent[j]:
                pi, wi = parent[i]
                pj, wj = parent[j]
                if m is None or (m and m < max(wi, wj)):
                    m = max(wi, wj)
                i = pi
                j = pj
            if parent[i] == parent[j] and i != j:
                if m is None or (m and m < max(parent[i][1], parent[j][1])):
                    m = max(parent[i][1], parent[j][1])

            ans.append(m)
        return ans












