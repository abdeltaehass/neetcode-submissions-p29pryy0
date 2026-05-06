class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(i, total):
            if i == len(nums):
                return 1 if total == target else 0

            if (i, total) in dp:
                return dp[(i, total)]

            add = dfs(i + 1, total + nums[i])
            subtract = dfs(i + 1, total - nums[i])

            dp[(i, total)] = add + subtract
            return dp[(i, total)]

        return dfs(0, 0)