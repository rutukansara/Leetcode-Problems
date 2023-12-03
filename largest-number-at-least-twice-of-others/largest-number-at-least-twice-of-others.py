class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        a = nums.index(max(nums))
        for i in range(len(nums)):
            if i !=a and nums[i] * 2 > nums[a]:
                return -1
        return a