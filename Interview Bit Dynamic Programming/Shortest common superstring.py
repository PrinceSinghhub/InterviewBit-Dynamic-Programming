class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        def overlappedString(a, b):
            resAB = None
            resBA = None

            lastPos = a.find(b[0])
            while lastPos >= 0:
                if a[lastPos:] == b[:len(a) - lastPos]:
                    resAB = a + b[len(a) - lastPos:]
                    break
                lastPos = a.find(b[0], lastPos + 1)
                # print("resAB", resAB)
            # print("a", a, "b", b)
            lastPos = b.find(a[0])
            # print("lastAinB", lastPos)
            while lastPos >= 0:
                if b[lastPos:] == a[:len(b) - lastPos]:
                    resBA = b + a[len(b) - lastPos:]
                    break
                lastPos = b.find(a[0], lastPos + 1)
                # print("resBA", resBA)
            if not resAB or not resBA:
                return resAB or resBA
            else:
                return resAB if len(resAB) < len(resBA) else resBA

        while len(A) > 1:
            maxOverlap = None, None, None
            for i, a in enumerate(A):

                for j, b in enumerate(A[i + 1:], i + 1):
                    overlap = overlappedString(a, b)
                    # print(s, t, overlap)
                    if overlap == None:
                        continue
                    if maxOverlap[0] is None or len(a) + len(b) - len(overlap) > maxOverlap[3]:
                        maxOverlap = i, j, overlap, len(a) + len(b) - len(overlap)

            if maxOverlap[0] is not None:
                # print("overlap", A[maxOverlap[0]], A[maxOverlap[1]], maxOverlap)
                A.pop(maxOverlap[1])
                A.pop(maxOverlap[0])
                A.append(maxOverlap[2])
            else:
                break

        # print(A)
        return sum(len(a) for a in A)
