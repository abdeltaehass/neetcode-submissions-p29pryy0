class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        past = {}

        for i , n in enumerate(nums):
            diff = target - n
            if diff in past:
                return [past[diff], i]
            past[n] = i