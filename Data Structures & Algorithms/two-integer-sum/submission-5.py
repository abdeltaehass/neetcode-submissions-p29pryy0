class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pastnums = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in pastnums:
                return [pastnums[diff], i]

            pastnums[num] = i