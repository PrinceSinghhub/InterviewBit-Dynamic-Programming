class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def solve(self, r, S):

        val, idx = min((val, idx) for (idx, val) in enumerate(S))
        ret = [idx] * (r // val)
        diff = r % val

        i = 0
        for j in range(idx):
            if diff == 0 or i == len(ret):
                break
            elif 0 < S[j] - val <= diff:
                while 0 < S[j] - val <= diff:
                    if i == len(ret):
                        break
                    ret[i] = j
                    i += 1
                    diff -= (S[j] - val)
        return ret
