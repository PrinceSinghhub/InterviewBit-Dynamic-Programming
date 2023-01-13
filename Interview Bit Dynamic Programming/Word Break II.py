class Solution:
    # @param A : string
    # @param B : list of strings
    # @return a list of strings
    def wordBreak(self, A, B):
        def go(s, wordDict, dic):
            res = []
            if s in dic:
                return dic[s]
            if (len(s) == 0):
                res.append("")
                return res
            for i in range(len(s), -1, -1):
                temp = s[i:]
                if (s[i:] in wordDict):
                    l = go(s[:i], wordDict, dic)
                    for x in l:
                        if (x == ""):
                            res.append(temp)
                        else:
                            res.append(x + " " + temp)

            dic[s] = res
            return res

        dic = {}
        return sorted(go(A, B, dic))




