class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for n in range(len(nums)):
            for m in range(0, len(nums)-n-1):
                if nums[m] > nums[m+1]:
                    nums[m], nums[m+1] = nums[m+1], nums[m]
        return nums