from functools import lru_cache
sys.setrecursionlimit(10000000)
class Solution:
    @lru_cache(1000000)
    def regmatch(self, i, j):
        if i == self.slen and j == self.plen: return 1
        if i == self.slen and j == self.plen-1 and self.p[j] == '*' : return 1
        if i == self.slen or j == self.plen: return 0
        if self.p[j] != '*':
            if self.s[i] == self.p[j] or self.p[j] == '?':
                return self.regmatch(i+1, j+1)
            else:
                return 0
        else:
            check = 0
            while(i < self.slen + 1):
                check = check or self.regmatch(i, j+1)
                i += 1
                if check == 1:
                    return 1
            return 0

    def isMatch(self, s, p):
        while '**' in p:
            p = p.replace('**', '*')
        self.s, self.p, self.slen, self.plen = s, p, len(s), len(p)
        if self.plen - p.count('*') > self.slen:
            return 0
        return self.regmatch(0, 0)
