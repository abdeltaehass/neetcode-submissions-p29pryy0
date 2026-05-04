class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False

        target = total // 2
        dp = {0}

        for num in nums:
            nextDP = set(dp)
            for t in dp:
                if t + num == target:
                    return True
                nextDP.add(t + num)
            dp = nextDP

        return target in dp
