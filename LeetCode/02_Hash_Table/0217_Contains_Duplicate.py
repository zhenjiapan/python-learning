class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        dict = {}
        for i, x in enumerate(nums):
            if x in dict:
                return True
            else:
                dict[x] = i
        return False
