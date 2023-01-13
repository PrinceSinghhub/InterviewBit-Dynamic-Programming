from collections import deque


class Solution:
    # @param A : string
    # @param B : list of strings
    # @return an integer
    def wordBreak(self, A, B):
        d = set(B)
        max_len = max(len(s) for s in d)
        valid = deque([0])
        for i in range(1, len(A) + 1):
            is_valid = False
            for pos in valid:
                if i - pos > max_len:
                    break
                if A[pos:i] in d:
                    is_valid = True
                    break

            if is_valid:
                valid.appendleft(i)

        return int(valid.popleft() == len(A))

