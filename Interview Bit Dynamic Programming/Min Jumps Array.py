class Solution:
    def find_dest(self,A,min_idx,max_idx):
        max_dest = 0
        for idx in range(min_idx,max_idx+1):
            if idx + A[idx]>max_dest:
                max_dest = idx + A[idx]
        return max_dest
    # @param A : list of integers
    # @return an integer
    def jump(self, A):
        lenA = len(A)
        if lenA==1: return 0
        min_dest = 1
        max_dest = A[0] #+0
        last_max_dest = 0
        num = 1
        while (max_dest < lenA-1) and (max_dest>last_max_dest):
            last_max_dest = max_dest
            max_dest = self.find_dest(A,min_dest,max_dest)
            min_dest = last_max_dest + 1
            num += 1
        if max_dest==last_max_dest: return -1
        else: return num

