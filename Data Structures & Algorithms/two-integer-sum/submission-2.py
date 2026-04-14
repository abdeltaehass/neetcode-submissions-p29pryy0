class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = [] 
        if len(nums) == 2:
            temp.append(0)
            temp.append(1)
            return temp
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                output = nums[i] + nums[j]
                if output == target:
                    temp.append(i)
                    temp.append(j)
                    return temp
