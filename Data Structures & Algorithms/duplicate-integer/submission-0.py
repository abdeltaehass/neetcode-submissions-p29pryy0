class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = []
        for i in nums:
            if i in temp:
                return True
            temp.append(i)
        return False

            