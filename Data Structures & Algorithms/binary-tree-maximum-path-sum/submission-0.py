# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")

        def dfs(node):
            nonlocal max_sum

            if not node:
                return 0

            # Ignore negative paths because they would lower the total.
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            # Best path that uses this node as the highest point.
            current_path = node.val + left_gain + right_gain
            max_sum = max(max_sum, current_path)

            # Return only one branch because the parent cannot use both.
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return max_sum