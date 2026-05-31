class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pastnum = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in pastnum:
                return [pastnum[complement], i]

            pastnum[num] = i