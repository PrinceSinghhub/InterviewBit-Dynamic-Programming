import bisect


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if self.subsetsum(A, B) == True:
            return 1
        else:
            return 0

    def remove(self, list, target):
        list.sort()
        try:
            del list[list.index(target) + 1:len(list)]
            return (list)
        except:
            del list[bisect.bisect_left(list, target):len(list)]
            return (list)

    # Returns the sum of the array
    def sumlist(self, list, target):
        self.remove(list, target)
        return (sum(list))

    # Main function - Returns Bool Value
    # Reduces array size by reducing the target value
    def subsetsum(self, alist, target):
        s = self.sumlist(alist, target)
        diff = s - target
        if s - target < 0:  # Target value can't be reached
            return False
        elif s == target:  # Elements in the array make up the target value
            return True
        elif s - target < target:  # Lowers the target value by making the difference of the sum(array) and target value the new target value
            target = diff
            if self.subsetsum(alist, target) == False:
                return False
            else:
                return True
        elif s >= target * 2:  # If sum(array) greater or equal to 2*target; algorithm stuck
            # Reset algo by removing greatest element from the array by test
            templist = list(alist)
            if self.subsetsum(templist, target - templist[-1]) == False:
                alist.pop()
                return True and self.subsetsum(alist, target)
            else:
                return True
        else:  # s-target > target
            if diff - target == target:  # diff - target <= target
                return True
            else:  # diff - target < target:
                target = diff - target
