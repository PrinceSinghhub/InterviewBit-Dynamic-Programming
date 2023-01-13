# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:

    def FindingMaxPathSum(self, root, Max):
        if root == None:
            return 0

    leftSum = max(0, self.FindingMaxPathSum(root.left, Max))
    rightSum = max(0, self.FindingMaxPathSum(root.right, Max))

    Max[0] = max(Max[0], (leftSum + rightSum + root.val))

    return root.val + max(leftSum, rightSum)


def maxPathSum(self, root):
    Max = [-10 ** 9]
    self.FindingMaxPathSum(root, Max)
    return Max[0]


