class Solution:
    # def twoSum(self, nums: list[int], target: int) -> list[int]:
    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict = {}
        for i, x in enumerate(nums):
            if target - x in dict:
                return [dict[target - x], i]
            else:
                dict[x] = i