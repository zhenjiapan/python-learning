class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] in nums[:i]:
                count += 1
            else:
                nums.insert(i-count, nums[i])
                nums.pop(i+1)
        return len(nums)-count