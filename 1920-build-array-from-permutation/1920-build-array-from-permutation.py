class Solution(object):
    def buildArray(self, nums):
        a = len(nums)
        range_a = range(a)
        ans = list(range_a)
        for i in nums:
            ans[i] = nums[nums[i]]
        return ans
        