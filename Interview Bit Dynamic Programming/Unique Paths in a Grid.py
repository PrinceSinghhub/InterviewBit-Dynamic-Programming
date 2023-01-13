from collections import deque
class Solution:
	# @param A : list of list of integers
	# @return an integer
    def __init__(self):
        self.total_path = 0
	def uniquePathsWithObstacles(self, A):

        def dfs(A, queue, visited):
            while queue:
                coor = queue.pop()
                row, col = coor
                if coor in visited:
                    continue
                if A[row][col] == 1:
                    continue
                if coor == (len(A) - 1, len(A[0]) - 1):
                    self.total_path += 1
                    continue
                visited.add(coor)
                if col + 1 < len(A[0]):
                    queue.append((row, col + 1))
                    dfs(A, queue.copy(), visited.copy())
                    queue.pop()
                if row + 1 < len(A):
                    queue.append((row + 1, col))
                    dfs(A, queue.copy(), visited.copy())
                    queue.pop()
        dfs(A, deque([(0,0)]), set())
        return self.total_path