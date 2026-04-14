class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pastnum = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in pastnum:
                return [pastnum[diff], i]
            pastnum[num] = i